import requests
import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings

logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def send_server_nfc(request):
    """
    NFCリクエストを処理する関数。
    フロントエンドの /api/nfc-request/ エンドポイント用。
    """
    try:
        # リクエストボディから学生IDを取得
        data = json.loads(request.body)
        student_id = data.get('student_id')
        
        if not student_id:
            return JsonResponse({
                'success': False,
                'error': '学生IDが指定されていません'
            }, status=400)
        
        # ======== 外部サーバーへのリクエスト設定 ========
        BASE_URL = getattr(settings, 'PARASHARE_API_URL', "http://chukyo-parashare.com:8000")
        endpoint = f"{BASE_URL}/students/{student_id}/auth"

        # ヘッダー
        headers = {
            "Content-Type": "application/json"
        }

        # 学生IDのバリデーション（基本的なチェック）
        if not str(student_id).isdigit() or len(str(student_id)) < 1:
            return JsonResponse({
                'success': False,
                'error': '無効な学生IDです'
            }, status=400)

        # ======== 外部サーバーへリクエスト送信 ========
        logger.info(f"NFCリクエスト送信: student_id={student_id}")
        response = requests.post(endpoint, headers=headers, timeout=10)
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
        error_details = None
        try:
            error_details = response.text if 'response' in locals() and response else None
        except:
            pass
        
        return JsonResponse({
            'success': False,
            'error': f'サーバーエラー: {e}',
            'details': error_details
        }, status=500)

    except requests.exceptions.RequestException as e:
        return JsonResponse({
            'success': False,
            'error': f'通信エラー: {e}'
        }, status=500)

    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': '無効なJSONデータです'
        }, status=400)

    except Exception as e:
        logger.error(f"予期しないエラー: {e}, student_id: {student_id if 'student_id' in locals() else 'unknown'}")
        return JsonResponse({
            'success': False,
            'error': '内部サーバーエラーが発生しました'
        }, status=500)