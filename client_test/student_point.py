import requests

# 固定設定
BASE_URL = "http://your-api-host.com"  # 本番環境なら適宜変更
student_id = "abc12345"  # NFCなどで読み取った学籍番号
endpoint = f"{BASE_URL}/students/{student_id}/auth"

# 認証または登録リクエストボディ
payload = {
    "stand_id": "123e4567-e89b-12d3-a456-426614174000",  # 傘スタンドUUID
    "mode": "auth"  # または "register"
}

# リクエスト送信
try:
    response = requests.post(endpoint, json=payload, timeout=5)
    response.raise_for_status()  # 200系以外を例外に

    data = response.json()
    print("✅ 認証結果:", data["data"])  # 例: {"registered": true, "student_name": "山田太郎"}
except requests.exceptions.HTTPError as http_err:
    print("❌ HTTPエラー:", http_err)
    print("詳細:", response.json())
except requests.exceptions.RequestException as err:
    print("❌ 通信エラー:", err)
