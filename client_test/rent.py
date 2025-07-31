from dotenv import load_dotenv
import os
import requests
import uuid

# ======== 設定 ========
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")  # デフォルト値を設定
rfid_tag = "01"          # NFCから読み取ったRFID
endpoint = f"{BASE_URL}/parasols/{rfid_tag}/rent"

# ========== リクエストデータ ==========
payload = {
    "student_id": "t323088",
    "stand_id": "ecb0107c-bb7d-4587-a7ca-4b10e51db92b" 
}

headers = {
    "Content-Type": "application/json"
}
# ========== 送信 ==========
try:
    response = requests.post(endpoint, json=payload, headers=headers,timeout=5)
    response.raise_for_status()
    result = response.json()

    print("貸出成功")
    print("返却期限:", result["data"]["due"])

except requests.exceptions.HTTPError as errh:
    print("HTTPエラー:", errh.response.status_code, errh.response.text)
except requests.exceptions.RequestException as e:
    print("通信エラー:", str(e))
