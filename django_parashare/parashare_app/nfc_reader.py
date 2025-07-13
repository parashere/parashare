import nfc
import re
import time
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def extract_student_id(tag_data):
    """NFCタグからStudentIDを抽出する"""
    pattern = re.compile(r"[A-Za-z]?\d{6,10}")  # 6～10桁の学籍番号のパターン
    for line in tag_data:
        match = pattern.search(line)
        if match:
            return match.group()
    return None

def on_connect(tag):
    """NFCタグ接続時の処理"""
    try:
        tag_data = tag.dump()
        student_id = extract_student_id(tag_data)
        print("学籍番号:", student_id)
        return {"success": True, "student_id": student_id}
    except Exception as e:
        print("タグ読み取りエラー:", e)
        return {"success": False, "error": str(e)}

@csrf_exempt
@require_http_methods(["POST"])
def read_nfc_tag(request):
    """NFC読み取りAPIエンドポイント"""
    try:
        with nfc.ContactlessFrontend("usb") as clf:
            print("NFCタグをかざしてください...")
            
            # タグ検出のタイムアウト設定（10秒）
            result = None
            
            def capture_tag(tag):
                nonlocal result
                result = on_connect(tag)
                return False  # タグ検出後に終了
            
            clf.connect(rdwr={"on-connect": capture_tag}, terminate=lambda: time.time() > time.time() + 10)
            
            if result and result["success"]:
                return JsonResponse({
                    "success": True,
                    "student_id": result["student_id"]
                })
            else:
                return JsonResponse({
                    "success": False,
                    "error": result["error"] if result else "タイムアウト"
                })
                
    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": f"NFC読み取りエラー: {str(e)}"
        })
