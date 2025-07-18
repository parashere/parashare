import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["POST"])
def send_server_nfc(request):
    """
    NFCリクエストを処理する関数。
    フロントエンドの /api/nfc-request/ エンドポイント用。
    """
    print("=== send_server_nfc function called ===")
    print(f"Request method: {request.method}")
    print(f"Request headers: {dict(request.headers)}")
    print(f"Request body: {request.body}")
    
    # デバッグ用：早期リターンテスト（一時的）
    # return JsonResponse({'success': True, 'message': 'Function called successfully'})
    
    try:
        # リクエストボディから学生IDを取得
        print("Parsing request body...")
        data = json.loads(request.body)
        print(f"Parsed data: {data}")
        student_id = data.get('student_id')
        print(f"Student ID: {student_id}")
        
        if not student_id:
            print("Student ID not found in request")
            return JsonResponse({
                'success': False,
                'error': '学生IDが指定されていません'
            }, status=400)
        
        # ======== 外部サーバーへのリクエスト設定 ========
        BASE_URL = "http://api.chukyo-parashare.com:8000"  # 本番では実際のAPIサーバーURLに変更
        endpoint = f"{BASE_URL}/students/{student_id}/auth"

        # ヘッダー
        headers = {
            "Content-Type": "application/json"
        }
        payload = {}
        # ======== 外部サーバーへリクエスト送信 ========
        print("sending NFC request to external server...")
        response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
        response.raise_for_status()

        # 成功レスポンス
        server_data = response.json()
        
        return JsonResponse({
            'success': True,
            'message': 'NFCリクエスト送信完了',
            'student_id': student_id,
            'server_response': server_data
        })

    except requests.exceptions.HTTPError as e:
        return JsonResponse({
            'success': False,
            'error': f'サーバーエラー: {e}',
            'details': response.text if 'response' in locals() else None
        }, status=500)

    except requests.exceptions.RequestException as e:
        return JsonResponse({
            'success': False,
            'error': f'通信エラー: {e}'
        }, status=500)

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return JsonResponse({
            'success': False,
            'error': '無効なJSONデータです'
        }, status=400)

    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return JsonResponse({
            'success': False,
            'error': f'予期しないエラー: {e}'
        }, status=500)