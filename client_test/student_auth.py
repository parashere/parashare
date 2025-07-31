from dotenv import load_dotenv
import os
import requests

# ======== 設定 ========
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")  # デフォルト値を設定
student_id = "t323088"  # NFCなどから取得した学籍番号
endpoint = f"{BASE_URL}/students/{student_id}/auth"

# ヘッダー（今回は署名なしなので最低限）
headers = {
    "Content-Type": "application/json"
}

# ======== リクエスト送信 ========
try:
    response = requests.post(endpoint, headers=headers, timeout=5)
    response.raise_for_status()

    # 結果表示
    data = response.json()
    status_code = response.status_code
    message = data.get("message", "")
    student_data = data.get("data", {})

    print(f"{status_code} ok:", message, student_data)

except requests.exceptions.HTTPError as e:
    print("HTTPエラー:", e)
    print("レスポンス:", response.text)

except requests.exceptions.RequestException as e:
    print("通信エラー:", e)

except Exception as e:
    print("その他のエラー:", e)
