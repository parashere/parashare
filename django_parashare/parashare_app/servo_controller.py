from django.http import JsonResponse
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
                logger.info(f"Servo initialized on pin {self.pin}")
            except Exception as e:
                logger.error(f"Failed to initialize servo: {e}")
                self.servo = None
        else:
            logger.info("Servo controller initialized in simulation mode")
    
    def open_gate(self):
        """ゲートを開く（右回転）"""
        try:
            if self.servo:
                logger.info("Opening gate (servo value: 1.0)")
                self.servo.value = 1.0
                sleep(2)  # 動作完了まで待機
                self.is_open = True
                return True
            else:
                logger.info("Simulating gate opening")
                self.is_open = True
                return True
        except Exception as e:
            logger.error(f"Failed to open gate: {e}")
            return False
    
    def close_gate(self):
        """ゲートを閉じる（左回転）"""
        try:
            if self.servo:
                logger.info("Closing gate (servo value: -1.0)")
                self.servo.value = -1.0
                sleep(2)  # 動作完了まで待機
                self.is_open = False
                return True
            else:
                logger.info("Simulating gate closing")
                self.is_open = False
                return True
        except Exception as e:
            logger.error(f"Failed to close gate: {e}")
            return False
    
    def get_status(self):
        """ゲートの状態を取得"""
        return {
            'is_open': self.is_open,
            'servo_available': SERVO_AVAILABLE,
            'servo_initialized': self.servo is not None
        }

# グローバルなサーボコントローラーインスタンス
servo_controller = ServoController()

def open_gate_api(request):
    """ゲートを開くAPI"""
    if request.method == 'POST':
        try:
            success = servo_controller.open_gate()
            return JsonResponse({
                'success': success,
                'message': 'ゲートを開きました' if success else 'ゲートの開放に失敗しました',
                'status': servo_controller.get_status()
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'エラーが発生しました: {str(e)}',
                'status': servo_controller.get_status()
            }, status=500)
    else:
        return JsonResponse({'error': 'POST method required'}, status=405)

def close_gate_api(request):
    """ゲートを閉じるAPI"""
    if request.method == 'POST':
        try:
            success = servo_controller.close_gate()
            return JsonResponse({
                'success': success,
                'message': 'ゲートを閉じました' if success else 'ゲートの閉鎖に失敗しました',
                'status': servo_controller.get_status()
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'エラーが発生しました: {str(e)}',
                'status': servo_controller.get_status()
            }, status=500)
    else:
        return JsonResponse({'error': 'POST method required'}, status=405)

def gate_status_api(request):
    """ゲートの状態を取得するAPI"""
    if request.method == 'GET':
        return JsonResponse({
            'success': True,
            'status': servo_controller.get_status()
        })
    else:
        return JsonResponse({'error': 'GET method required'}, status=405)
