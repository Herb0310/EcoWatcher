import fastapi
from render_get_token import get_token,get_hh_readings,get_date

OCTOPUS_URL = "https://api.oejp-kraken.energy/v1/graphql/"
OCTOPUS_EMAIL = "pad.supert0310@gmail.com"
OCTOPUS_PASSWORD = "Supert0310"
OCTOPUS_NUMBER = "A-A619AE23"

app = fastapi.FastAPI()

@app.get("/")
def main():
    # メイン処理
    token = get_token()
    days = get_date()
    hh = get_hh_readings(OCTOPUS_NUMBER,token,days[0],days[1])
    print(hh)

main()