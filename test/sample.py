

def get_data():
    # 取得データから電気使用量、電気代を抽出する
    token = get_token()
    d = get_date() 
    readings = get_hh_readings(
    account_number=OCTOPUS_ACCOUNT_NUMBER,
    token=token,
    start_at=d[0],
    end_at=d[1],
    )
    return readings

def send_message():
    # LINEに送信する

    pass

