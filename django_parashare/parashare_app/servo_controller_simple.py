from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import logging
from time import sleep

logger = logging.getLogger(__name__)

# Raspberry Pi環境でのみgpiozeroを使用
try:
    from gpiozero import Servo
    from gpiozero.pins.pigpio import PiGPIOFactory
    SERVO_AVAILABLE = True
except ImportError:
    SERVO_AVAILABLE = False
    logger.warning("gpiozero not available. Servo control will be simulated.")

class ServoController:
    def __init__(self, pin=13):
        self.pin = pin
        self.servo = None
        self.is_open = False
        self.logs = []  # ログメッセージを保存するリスト
        
        if SERVO_AVAILABLE:
            try:
                factory = PiGPIOFactory()
                # サーボの制御範囲を拡張（0.5ms～2.5msのパルス幅）
                self.servo = Servo(
                    pin=self.pin, 
                    pin_factory=factory,
                    min_pulse_width=0.5/1000,  # 0.5ms
                    max_pulse_width=2.5/1000   # 2.5ms
                )
                #self.servo.value = 0.0  # 初期位置（中央）
                sleep(1)
                log_msg = f"Servo initialized on pin {self.pin} with PiGPIOFactory (extended range)"
                logger.info(log_msg)
                self.logs.append(log_msg)
            except Exception as e:
                log_msg = f"Failed to initialize servo: {e}"
                logger.error(log_msg)
                self.logs.append(log_msg)
                self.servo = None
        else:
            log_msg = "Servo controller in simulation mode"
            logger.info(log_msg)
            self.logs.append(log_msg)
    
    def open_gate(self):
        """ゲートを開く"""
        try:
            if self.servo:
                self.servo.value = 0.0  # 最大位置
                sleep(2)
            else:
                sleep(1)  # シミュレーション
            
            self.is_open = True
            log_msg = "Gate opened (1.0)"
            logger.info(log_msg)
            self.logs.append(log_msg)
            return True
        except Exception as e:
            log_msg = f"Failed to open gate: {e}"
            logger.error(log_msg)
            self.logs.append(log_msg)
            return False
    
    def close_gate(self):
        """ゲートを閉じる"""
        try:
            if self.servo:
               # ここでサーボモータ設定
               
            else:
                sleep(1)  # シミュレーション
            
            self.is_open = False
            log_msg = "Gate closed (-1.0)"
            logger.info(log_msg)
            self.logs.append(log_msg)
            return True
        except Exception as e:
            log_msg = f"Failed to close gate: {e}"
            logger.error(log_msg)
            self.logs.append(log_msg)
            return False
    
    def get_status(self):
        """ゲートの状態を取得"""
        return {
            'is_open': self.is_open,
            'servo_available': SERVO_AVAILABLE,
            'servo_initialized': self.servo is not None,
            'pin': self.pin,
            'logs': self.logs[-10:]  # 最新の10件のログを返す
        }

# グローバルなサーボコントローラーインスタンス（遅延初期化）
servo_controller = None

def get_servo_controller():
    """サーボコントローラーのシングルトンインスタンスを取得"""
    global servo_controller
    if servo_controller is None:
        init_msg = "📡 サーボコントローラーを初期化中..."
        print(init_msg)
        servo_controller = ServoController()
        complete_msg = "✅ サーボコントローラー初期化完了"
        print(complete_msg)
        servo_controller.logs.append(init_msg)
        servo_controller.logs.append(complete_msg)
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
            'status': controller.get_status(),
            'logs': controller.logs[-5:]  # 最新の5件のログ
        })
    except Exception as e:
        error_msg = f'エラーが発生しました: {str(e)}'
        return JsonResponse({
            'success': False,
            'message': error_msg,
            'logs': [error_msg]
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
            'status': controller.get_status(),
            'logs': controller.logs[-5:]  # 最新の5件のログ
        })
    except Exception as e:
        error_msg = f'エラーが発生しました: {str(e)}'
        return JsonResponse({
            'success': False,
            'message': error_msg,
            'logs': [error_msg]
        }, status=500)

@require_http_methods(["GET"])
def gate_status_api(request):
    """ゲートの状態を取得するAPI"""
    try:
        controller = get_servo_controller()
        return JsonResponse({
            'success': True,
            'status': controller.get_status(),
            'logs': controller.logs[-10:]  # 最新の10件のログ
        })
    except Exception as e:
        error_msg = f'エラーが発生しました: {str(e)}'
        return JsonResponse({
            'success': False,
            'message': error_msg,
            'logs': [error_msg]
        }, status=500)
