from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import logging

logger = logging.getLogger(__name__)

# Raspberry Pi環境でのみgpiozeroを使用
try:
    from gpiozero import Servo
    from time import sleep
    SERVO_AVAILABLE = True
except ImportError:
    SERVO_AVAILABLE = False
    logger.warning("gpiozero not available. Servo control will be simulated.")

class ServoController:
    def __init__(self, pin=13):
        self.pin = pin
        self.servo = None
        self.is_open = False
        
        if SERVO_AVAILABLE:
            try:
                self.servo = Servo(pin=self.pin)
                print(f"✓ Servo initialized successfully on pin {self.pin}")
                logger.info(f"Servo initialized on pin {self.pin}")
            except Exception as e:
                print(f"❌ Failed to initialize servo: {e}")
                logger.error(f"Failed to initialize servo: {e}")
                self.servo = None
        else:
            print("⚠ gpiozero not available. Running in simulation mode.")
            logger.info("Servo controller initialized in simulation mode")
    
    def open_gate(self):
        """ゲートを開く（右回転）"""
        try:
            if self.servo:
                print("🔄 Opening gate - Setting servo to maximum position (1.0)")
                logger.info("Opening gate (servo value: 1.0)")
                self.servo.value = 1.0
                print(f"⏱ Waiting 2 seconds for servo movement...")
                sleep(2)  # 動作完了まで待機
                print("✓ Gate opened successfully")
                self.is_open = True
                return True
            else:
                print("🎭 Simulating gate opening (no physical servo)")
                logger.info("Simulating gate opening")
                sleep(1)  # シミュレーション用の短い待機
                self.is_open = True
                return True
        except Exception as e:
            print(f"❌ Failed to open gate: {e}")
            logger.error(f"Failed to open gate: {e}")
            return False
    
    def close_gate(self):
        """ゲートを閉じる（左回転）"""
        try:
            if self.servo:
                print("🔄 Closing gate - Setting servo to minimum position (-1.0)")
                logger.info("Closing gate (servo value: -1.0)")
                self.servo.value = -1.0
                print(f"⏱ Waiting 2 seconds for servo movement...")
                sleep(2)  # 動作完了まで待機
                print("✓ Gate closed successfully")
                self.is_open = False
                return True
            else:
                print("🎭 Simulating gate closing (no physical servo)")
                logger.info("Simulating gate closing")
                sleep(1)  # シミュレーション用の短い待機
                self.is_open = False
                return True
        except Exception as e:
            print(f"❌ Failed to close gate: {e}")
            logger.error(f"Failed to close gate: {e}")
            return False
    
    def get_status(self):
        """ゲートの状態を取得"""
        status = {
            'is_open': self.is_open,
            'servo_available': SERVO_AVAILABLE,
            'servo_initialized': self.servo is not None,
            'pin': self.pin,
            'current_value': getattr(self.servo, 'value', None) if self.servo else None
        }
        print(f"📊 Current status: {status}")
        return status
    
    def test_servo(self):
        """サーボテスト用関数"""
        if not self.servo:
            print("❌ No servo available for testing")
            return False
        
        try:
            print("🧪 Testing servo movement...")
            # 中央位置
            print("→ Moving to center (0.0)")
            self.servo.value = 0.0
            sleep(1)
            
            # 右端
            print("→ Moving to right (1.0)")
            self.servo.value = 1.0
            sleep(1)
            
            # 左端
            print("→ Moving to left (-1.0)")
            self.servo.value = -1.0
            sleep(1)
            
            # 中央に戻す
            print("→ Returning to center (0.0)")
            self.servo.value = 0.0
            sleep(1)
            
            print("✓ Servo test completed successfully")
            return True
        except Exception as e:
            print(f"❌ Servo test failed: {e}")
            return False

# グローバルなサーボコントローラーインスタンス
servo_controller = ServoController()

@csrf_exempt
@require_http_methods(["GET", "POST"])
def open_gate_api(request):
    """ゲートを開くAPI"""
    # CORS対応
    response_data = {}
    
    if request.method == 'POST':
        try:
            success = servo_controller.open_gate()
            response_data = {
                'success': success,
                'message': 'ゲートを開きました' if success else 'ゲートの開放に失敗しました',
                'status': servo_controller.get_status(),
                'method': 'POST'
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': f'エラーが発生しました: {str(e)}',
                'status': servo_controller.get_status(),
                'method': 'POST'
            }
            return JsonResponse(response_data, status=500)
    elif request.method == 'GET':
        # GETでの疎通テスト
        response_data = {
            'success': True,
            'message': 'Servo open API is working',
            'method': 'GET',
            'status': servo_controller.get_status()
        }
    
    response = JsonResponse(response_data)
    # CORS対応ヘッダーを追加
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@csrf_exempt
@require_http_methods(["GET", "POST"])
def close_gate_api(request):
    """ゲートを閉じるAPI"""
    # CORS対応
    response_data = {}
    
    if request.method == 'POST':
        try:
            success = servo_controller.close_gate()
            response_data = {
                'success': success,
                'message': 'ゲートを閉じました' if success else 'ゲートの閉鎖に失敗しました',
                'status': servo_controller.get_status(),
                'method': 'POST'
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': f'エラーが発生しました: {str(e)}',
                'status': servo_controller.get_status(),
                'method': 'POST'
            }
            return JsonResponse(response_data, status=500)
    elif request.method == 'GET':
        # GETでの疎通テスト
        response_data = {
            'success': True,
            'message': 'Servo close API is working',
            'method': 'GET',
            'status': servo_controller.get_status()
        }
    
    response = JsonResponse(response_data)
    # CORS対応ヘッダーを追加
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

def gate_status_api(request):
    """ゲートの状態を取得するAPI"""
    if request.method == 'GET':
        return JsonResponse({
            'success': True,
            'status': servo_controller.get_status()
        })
    else:
        return JsonResponse({'error': 'GET method required'}, status=405)

@csrf_exempt
def test_servo_api(request):
    """サーボテスト用API"""
    if request.method == 'POST':
        try:
            success = servo_controller.test_servo()
            return JsonResponse({
                'success': success,
                'message': 'サーボテスト完了' if success else 'サーボテスト失敗',
                'status': servo_controller.get_status()
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'テストエラー: {str(e)}',
                'status': servo_controller.get_status()
            }, status=500)
    else:
        return JsonResponse({'error': 'POST method required'}, status=405)
