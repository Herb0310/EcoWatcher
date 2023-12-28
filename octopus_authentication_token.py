from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import json 
import os
import sys
import dotenv
import requests
from datetime import datetime, timedelta

# Load .env file
dotenv.load_dotenv()

class OctopusAuthenticationToken:
    # GraphQL endpoint URL
    GRAPHQL_URL = "https://api.oejp-kraken.energy/v1/graphql/"

    def generate_token(self):
        # GraphQL mutation query
        mutation_query = '''
            mutation($input: ObtainJSONWebTokenInput!) {
                obtainKrakenToken(input: $input) {
                    token
                    refreshToken
                }
            }
        '''

        # GraphQL variables
        variables = {
            "input": {
                "email": os.environ.get("OCTOPUS_EMAIL"),
                "password": os.environ.get("OCTOPUS_PASSWORD")
            }
        }

        # GraphQL request payload
        payload = {
            "query": mutation_query,
            "variables": variables
        }

        # Make the GraphQL request
        response = requests.post(self.GRAPHQL_URL, json=payload)

        # Check for errors in the response
        response.raise_for_status()

        # Parse the JSON response
        result = response.json()

        # Extract the token from the result
        token = result.get("data", {}).get("obtainKrakenToken", {}).get("token")
        #refreshToken = result.get("data", {}).get("obtainKrakenToken", {}).get("refreshToken")

        return token

class OctopusEnergyBillController:
    http_transport = AIOHTTPTransport(
        url="https://api.oejp-kraken.energy/v1/graphql/",
        headers={"Authorization": OctopusAuthenticationToken().generate_token()}
    )

    client = Client(transport=http_transport, fetch_schema_from_transport=True)

    @staticmethod
    def get_bill_query():
        return gql('''
            query(
                $accountNumber: String!
                $fromDatetime: DateTime
                $toDatetime: DateTime
            ) {
                account(accountNumber: $accountNumber) {
                    properties {
                        electricitySupplyPoints {
                            agreements {
                                validFrom
                            }
                            halfHourlyReadings(
                                fromDatetime: $fromDatetime
                                toDatetime: $toDatetime
                            ) {
                                startAt
                                endAt
                                value
                                costEstimate
                                consumptionStep
                                consumptionRateBand
                            }
                        }
                    }
                }
            }
        ''')

    def index(self):
        query = OctopusEnergyBillController.get_bill_query()

        # Use string representation of datetime objects
        from_datetime = (datetime.now() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
        to_datetime = datetime.now().replace(hour=0 ,minute=0, second=0, microsecond=0).isoformat()
        
        result = OctopusEnergyBillController.client.execute(query, variable_values={
            'accountNumber': os.environ.get("OCTOPUS_ACCOUNT_NUMBER"),
            'fromDatetime': from_datetime + ".000Z",
            'toDatetime': to_datetime + ".000Z"
        })

        properties = result.get("account", {}).get("properties", [])
        electricity_supply_points = properties[0].get("electricitySupplyPoints", [])
        half_hourly_readings = electricity_supply_points[0].get("halfHourlyReadings", [])

        kwh = sum(float(reading["value"]) for reading in half_hourly_readings)
        cost = sum(float(reading["costEstimate"]) for reading in half_hourly_readings)

        print(f"{(datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')}は{kwh:.2f}kWh消費して{cost:.2f}円かかったよ")

# インスタンスを生成して実行
controller = OctopusEnergyBillController()
controller.index()

