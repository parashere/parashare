import requests

#BASE_URL = "http://localhost:8000"
BASE_URL = "http://150.42.11.227:8000/"

rfid = "RFID001"
endpoint = f"{BASE_URL}/parasols/{rfid}/rent"

payload = {
    "student_id": "t323088",  # 実際に存在する学籍番号
    "stand_id": "a842c4ac-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # 実在するスタンドID（UUID文字列）
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(endpoint, json=payload, headers=headers, timeout=5)
    response.raise_for_status()
    print(f"{response.status_code} OK")
    print(response.json())

except requests.exceptions.HTTPError as errh:
    print("HTTPエラー:", errh)
    print("レスポンス:", response.text)
