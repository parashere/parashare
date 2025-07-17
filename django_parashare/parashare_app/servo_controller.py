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
        self.current_position = 0.0  # 現在位置を追跡
        
        print(f"🔧 サーボコントローラー初期化開始 (ピン: {pin})")
        
        if SERVO_AVAILABLE:
            try:
                print(f"📡 GPIOピン {pin} でサーボを初期化中...")
                self.servo = Servo(pin=self.pin)
                
                # 初期位置を設定（中央）
                print("🎯 初期位置（中央: 0.0）に設定中...")
                self.servo.value = 0.0
                self.current_position = 0.0
                sleep(1)  # 位置安定のための待機
                
                print(f"✅ サーボ初期化成功！ピン: {self.pin}, 初期位置: {self.current_position}")
                logger.info(f"Servo initialized on pin {self.pin}")
            except Exception as e:
                print(f"❌ サーボ初期化失敗: {e}")
                print(f"💡 可能な原因: GPIO権限、配線、電源供給")
                logger.error(f"Failed to initialize servo: {e}")
                self.servo = None
        else:
            print("⚠️  gpiozero利用不可 - シミュレーションモードで動作")
            print("💻 実機テストには Raspberry Pi + gpiozero が必要です")
            logger.info("Servo controller initialized in simulation mode")
    
    def open_gate(self):
        """ゲートを開く（右回転）"""
        try:
            if self.servo:
                print("� ゲート開放開始...")
                print("🔄 サーボを最大位置 (1.0) に設定中...")
                logger.info("Opening gate (servo value: 1.0)")
                
                self.servo.value = 1.0
                self.current_position = 1.0
                
                print(f"⏳ 動作完了まで2秒待機...")
                sleep(2)  # 動作完了まで待機
                
                print("✅ ゲート開放完了！")
                self.is_open = True
                return True
            else:
                print("🎭 ゲート開放をシミュレーション中...")
                logger.info("Simulating gate opening")
                self.current_position = 1.0
                sleep(1)  # シミュレーション用の短い待機
                self.is_open = True
                return True
        except Exception as e:
            print(f"❌ ゲート開放失敗: {e}")
            logger.error(f"Failed to open gate: {e}")
            return False
    
    def close_gate(self):
        """ゲートを閉じる（左回転）"""
        try:
            if self.servo:
                print("� ゲート閉鎖開始...")
                print("🔄 サーボを最小位置 (-1.0) に設定中...")
                logger.info("Closing gate (servo value: -1.0)")
                
                self.servo.value = -1.0
                self.current_position = -1.0
                
                print(f"⏳ 動作完了まで2秒待機...")
                sleep(2)  # 動作完了まで待機
                
                print("✅ ゲート閉鎖完了！")
                self.is_open = False
                return True
            else:
                print("🎭 ゲート閉鎖をシミュレーション中...")
                logger.info("Simulating gate closing")
                self.current_position = -1.0
                sleep(1)  # シミュレーション用の短い待機
                self.is_open = False
                return True
        except Exception as e:
            print(f"❌ ゲート閉鎖失敗: {e}")
            logger.error(f"Failed to close gate: {e}")
            return False
    
    def get_status(self):
        """ゲートの状態を取得"""
        # 実際のサーボ値を取得（可能であれば）
        actual_servo_value = None
        if self.servo:
            try:
                actual_servo_value = self.servo.value
            except:
                actual_servo_value = "読み取り不可"
        
        status = {
            'is_open': self.is_open,
            'servo_available': SERVO_AVAILABLE,
            'servo_initialized': self.servo is not None,
            'pin': self.pin,
            'current_value': actual_servo_value if actual_servo_value is not None else self.current_position,
            'tracked_position': self.current_position,
            'servo_object_exists': self.servo is not None
        }
        print(f"📊 現在の詳細状態:")
        print(f"   ゲート状態: {'開' if status['is_open'] else '閉'}")
        print(f"   ピン番号: {status['pin']}")
        print(f"   サーボ利用可能: {status['servo_available']}")
        print(f"   サーボ初期化済み: {status['servo_initialized']}")
        print(f"   実際のサーボ値: {actual_servo_value}")
        print(f"   追跡中の位置: {status['tracked_position']}")
        return status
    
    def test_servo(self):
        """サーボテスト用関数"""
        if not self.servo:
            print("❌ 物理サーボが利用できません（シミュレーションモード）")
            print("🎭 シミュレーションテストを実行します...")
            
            positions = [0.0, 1.0, -1.0, 0.0]
            names = ["中央", "右端（開）", "左端（閉）", "中央（復帰）"]
            
            for pos, name in zip(positions, names):
                print(f"→ {name} ({pos}) に移動中...")
                self.current_position = pos
                sleep(0.5)
            
            print("✅ シミュレーションテスト完了")
            return True
        
        try:
            print("🧪 物理サーボの動作テストを開始...")
            
            # テスト用の位置と名称
            test_positions = [
                (0.0, "中央位置"),
                (1.0, "右端位置（ゲート開）"), 
                (-1.0, "左端位置（ゲート閉）"),
                (0.0, "中央位置（復帰）")
            ]
            
            for position, description in test_positions:
                print(f"→ {description} ({position}) に移動中...")
                self.servo.value = position
                self.current_position = position
                sleep(1.5)  # 各位置で少し長めに待機
                
                # 位置確認
                try:
                    actual_value = self.servo.value
                    print(f"   ✓ 設定完了 (実際の値: {actual_value})")
                except:
                    print(f"   ⚠ 値の読み取り不可（設定は完了）")
            
            print("✅ 物理サーボテスト完了")
            return True
            
        except Exception as e:
            print(f"❌ サーボテスト失敗: {e}")
            return False
    
    def set_position(self, value):
        """指定した位置にサーボを設定"""
        try:
            # 値の範囲チェック
            if not (-1.0 <= value <= 1.0):
                print(f"❌ 値の範囲エラー: {value} （-1.0から1.0の範囲で指定してください）")
                return False
            
            if self.servo:
                print(f"🎯 サーボを位置 {value} に設定中...")
                self.servo.value = value
                self.current_position = value
                sleep(1)  # 移動時間を確保
                print(f"✅ 位置設定完了: {value}")
                return True
            else:
                print(f"🎭 シミュレーション: 位置 {value} に設定")
                self.current_position = value
                return True
                
        except Exception as e:
            print(f"❌ 位置設定失敗: {e}")
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

@csrf_exempt
def set_position_api(request):
    """手動位置設定API"""
    if request.method == 'POST':
        try:
            import json
            data = json.loads(request.body)
            position = data.get('position', 0.0)
            
            success = servo_controller.set_position(position)
            return JsonResponse({
                'success': success,
                'message': f'位置 {position} に設定しました' if success else f'位置設定に失敗: {position}',
                'position': position,
                'status': servo_controller.get_status()
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'位置設定エラー: {str(e)}',
                'status': servo_controller.get_status()
            }, status=500)
    else:
        return JsonResponse({'error': 'POST method required'}, status=405)
