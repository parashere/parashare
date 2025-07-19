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
                self.servo.value = 0.0  # 初期位置（中央）
                sleep(1)
                logger.info(f"Servo initialized on pin {self.pin}")
            except Exception as e:
                logger.error(f"Failed to initialize servo: {e}")
                self.servo = None
        else:
            logger.info("Servo controller in simulation mode")
    
    def open_gate(self):
        """ゲートを開く"""
        try:
            if self.servo:
                self.servo.value = 1.0  # 最大位置
                sleep(2)
            else:
                sleep(1)  # シミュレーション
            
            self.is_open = True
            logger.info("Gate opened")
            return True
        except Exception as e:
            logger.error(f"Failed to open gate: {e}")
            return False
    
    def close_gate(self):
        """ゲートを閉じる"""
        try:
            if self.servo:
                self.servo.value = -1.0  # 最小位置
                sleep(2)
            else:
                sleep(1)  # シミュレーション
            
            self.is_open = False
            logger.info("Gate closed")
            return True
        except Exception as e:
            logger.error(f"Failed to close gate: {e}")
            return False
    
    def get_status(self):
        """ゲートの状態を取得"""
        return {
            'is_open': self.is_open,
            'servo_available': SERVO_AVAILABLE,
            'servo_initialized': self.servo is not None,
            'pin': self.pin
        }

# グローバルなサーボコントローラーインスタンス（遅延初期化）
servo_controller = None

def get_servo_controller():
    """サーボコントローラーのシングルトンインスタンスを取得"""
    global servo_controller
    if servo_controller is None:
        print("📡 サーボコントローラーを初期化中...")
        servo_controller = ServoController()
        print("✅ サーボコントローラー初期化完了")
    return servo_controller

@csrf_exempt
@require_http_methods(["POST"])
def open_gate_api(request):
    """ゲートを開くAPI"""
    try:
        controller = get_servo_controller()
        success = controller.open_gate()
        return JsonResponse({
            'success': success,
            'message': 'ゲートを開きました' if success else 'ゲートの開放に失敗しました',
            'status': controller.get_status()
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'エラーが発生しました: {str(e)}'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def close_gate_api(request):
    """ゲートを閉じるAPI"""
    try:
        controller = get_servo_controller()
        success = controller.close_gate()
        return JsonResponse({
            'success': success,
            'message': 'ゲートを閉じました' if success else 'ゲートの閉鎖に失敗しました',
            'status': controller.get_status()
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'エラーが発生しました: {str(e)}'
        }, status=500)

@require_http_methods(["GET"])
def gate_status_api(request):
    """ゲートの状態を取得するAPI"""
    controller = get_servo_controller()
    return JsonResponse({
        'success': True,
        'status': controller.get_status()
    })
