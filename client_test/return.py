import requests
import uuid

# ========== 設定 ==========
BASE_URL = "http://127.0.0.1:8000"  # FastAPIのURL
rfid_tag = "01"  # 返却する傘のRFID（例: NFCで読み取った値）

endpoint = f"{BASE_URL}/parasols/{rfid_tag}/return"

# ========== リクエストデータ ==========
payload = {
    "student_id": "t323088",
    "stand_id": "ecb0107c-bb7d-4587-a7ca-4b10e51db92b"
}

headers = {
    "Content-Type": "application/json"
}

# ========== リクエスト送信 ==========
try:
    response = requests.post(endpoint, json=payload, headers=headers, timeout=5)
    response.raise_for_status()
    result = response.json()

    print("返却成功")
    print("サーバーメッセージ:", result.get("message", ""))
    print("返却日時:", result["data"]["returned_at"])

except requests.exceptions.HTTPError as errh:
    print("HTTPエラー:", errh.response.status_code, errh.response.text)
except requests.exceptions.RequestException as e:
    print("通信エラー:", str(e))
