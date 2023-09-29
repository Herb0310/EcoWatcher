import os
import dataclasses
import decimal
import requests
import datetime
import pytz
from typing import List, Optional

from rich import console as rich_console
from rich import table as rich_table
from rich import text as rich_text

@dataclasses.dataclass(frozen=True)
class HHReading:
    start_at: datetime.datetime
    end_at: datetime.datetime
    version: str
    value: decimal.Decimal

#OCTOPUS_URL = os.environ["API_URL"]
#OCTOPUS_EMAIL = os.environ["OCTOPUS_EMAIL"]
#OCTOPUS_PASSWORD = os.environ["OCTOPUS_PASSWORD"]
#OCTOPUS_ACCOUNT_NUMBER = os.environ["OCTOPUS_ACCOUNT_NUMBER"]
OCTOPUS_URL = "https://api.oejp-kraken.energy/v1/graphql/"
OCTOPUS_EMAIL = "pad.supert0310@gmail.com"
OCTOPUS_PASSWORD = "Supert0310"
OCTOPUS_ACCOUNT_NUMBER = "A-A619AE23"

AUTH_BODY = """
mutation obtainKrakenToken($input: ObtainJSONWebTokenInput!) {
  obtainKrakenToken(input: $input) {
    refreshToken
    refreshExpiresIn
    payload
    token
  }
}
"""

GET_HH_BODY = """
query halfHourlyReadings($accountNumber: String!, $fromDatetime: DateTime, $toDatetime: DateTime) {
  account(accountNumber: $accountNumber) {
    properties {
      electricitySupplyPoints {
        halfHourlyReadings(fromDatetime: $fromDatetime, toDatetime: $toDatetime) {
          startAt
          endAt
          version
          value
        }
      }
    }
  }
}
""" 

def _validate_response(response: requests.Response) -> None:
    # 
    if (errors := response.json().get("errors")) and len(errors):
        raise ValueError(errors)

def get_token() -> str:
    # 認証トークンの発行(1時間で有効期限が切れるので実行毎に発行が必要)
    response = requests.post(
        url=OCTOPUS_URL,
        json={
            "query": AUTH_BODY,
            "variables": {
                "input": {
                    "email": OCTOPUS_EMAIL,
                    "password": OCTOPUS_PASSWORD,
                }
            },
        },
    )
    response_dict = response.json()
    _validate_response(response)

    return response_dict["data"]["obtainKrakenToken"]["token"]

def get_hh_readings(
    account_number: str,
    token: str,
    start_at: datetime.datetime,
    end_at:  Optional[datetime.datetime] = None,) -> List[HHReading]:
    variables = {
        "accountNumber": account_number,
        "fromDatetime": start_at.isoformat(),
    }
    if end_at:
        variables["toDatetime"] = end_at.isoformat()
    response = requests.post(
        url=OCTOPUS_URL,
        json={
            "query": GET_HH_BODY,
            "variables": variables,
        },
        headers={"authorization": f"JWT {token}"},
    )
    _validate_response(response)

    response_dict = response.json()
    readings_raw = response_dict["data"]["account"]["properties"][0]["electricitySupplyPoints"][0]["halfHourlyReadings"]
    readings: List[HHReading] = []
    for reading_raw in readings_raw:
        readings.append(
            HHReading(
                start_at=datetime.datetime.fromisoformat(reading_raw["startAt"]),
                end_at=datetime.datetime.fromisoformat(reading_raw["endAt"]),
                version=reading_raw["version"],
                value=decimal.Decimal(reading_raw["value"]),
            )
        )

    return readings

def _calculate_daily_average(readings: List[octopus.HHReading]) -> float:
    """
    Return the daily average electricity usage.
    """
    daily_usage = defaultdict(list)
    for reading in readings:
        daily_usage[reading.start_at.date()].append(reading.value)
    return statistics.fmean([sum(reading) for reading in daily_usage.values()])

def print_electricity_usage(
    start_date: datetime.date, end_date: Optional[datetime.date] = None
):
    """
    Print electricity usage statistics.
    """

    readings = _get_readings(start_date, end_date)

    # Prepare usage table.
    usage_table = _build_usage_table(start_date, end_date)
    usage_table.add_row(
        rich_text.Text("Daily Avg", style=PINK, justify="left"),
        rich_text.Text(
            f"{_calculate_daily_average(readings=readings):.2f} kWh",
            justify="right",
        ),
    )
    usage_table.add_row(
        rich_text.Text("Total Usage", style=PURPLE, justify="left"),
        rich_text.Text(
            f"{_calculate_total_usage(readings=readings):.2f} kWh",
            justify="right",
        ),
    )

    console = rich_console.Console(record=True, width=30)
    console.print(usage_table)
    with open("usage.svg", "w") as f:
        f.write(console.export_svg(title="Electricity Usage"))



def get_date():
    # 日付を取得する
#    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    now = datetime.datetime.now()
    today = now.date()
    yesterday = now + datetime.timedelta(days=-1)
    yesterday = yesterday.date()
    bomonth = now.strftime('%Y-%m-01')
    return today,yesterday

