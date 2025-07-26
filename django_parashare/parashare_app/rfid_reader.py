import time
import json
import logging
from collections import Counter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)

# RFID環境の可用性チェック
try:
    import serial
    RFID_AVAILABLE = True
except ImportError:
    RFID_AVAILABLE = False
    logger.warning("pyserial not available. RFID reading will be simulated.")

class RFIDReader:
    def __init__(self, port='/dev/ttyACM0', baud_rate=115200):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = None
        self.logs = []

    def connect(self):
        """シリアルポートに接続"""
        if not RFID_AVAILABLE:
            log_msg = "RFID reader in simulation mode (pyserial not available)"
            logger.info(log_msg)
            self.logs.append(log_msg)
            return True  # シミュレーションモードでは成功として扱う
            
        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=0.8)  # タイムアウトを短縮
            log_msg = f"RFID Reader connected to {self.port}"
            logger.info(log_msg)
            self.logs.append(log_msg)
            return True
        except serial.SerialException as e:
            log_msg = f"Failed to connect to RFID Reader: {e}"
            logger.error(log_msg)
            self.logs.append(log_msg)
            return False

    def disconnect(self):
        """シリアルポートを切断"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            log_msg = "RFID Reader disconnected"
            logger.info(log_msg)
            self.logs.append(log_msg)

    def read_single_tag(self):
        """1回だけタグを読み取る"""
        if not self.ser or not self.ser.is_open:
            return None
            
        try:
            # バッファをクリア
            self.ser.reset_input_buffer()
            
            # コマンドを送信
            command_to_send = bytes([0x7C, 0xFF, 0xFF, 0x20, 0x00, 0x00, 0x66])
            self.ser.write(command_to_send)
            
            # 応答を待つ（時間短縮）
            time.sleep(0.05)  # 0.1から0.05に短縮
            response = self.ser.read(128)
            
            if response and response.startswith(b'\xCC\xFF\xFF\x20\x02'):
                epc_start_index = 10
                epc_length = 12
                epc_end_index = epc_start_index + epc_length
                if len(response) >= epc_end_index:
                    epc = response[epc_start_index:epc_end_index]
                    return epc.hex().upper()
        except Exception as e:
            log_msg = f"Error reading RFID tag: {e}"
            logger.error(log_msg)
            self.logs.append(log_msg)
            return None
        return None

    def read_multiple_tags(self, count=3):
        """複数回タグを読み取り、最も多く検出されたIDを返す"""
        if not self.connect():
            return None, []

        try:
            tag_ids = []
            read_attempts = []
            
            log_msg = f"Starting {count} RFID reads..."
            logger.info(log_msg)
            self.logs.append(log_msg)
            
            # 指定回数読み取りを実行
            for i in range(count):
                tag_id = self.read_single_tag()
                attempt_log = f"[{i+1:2d}回目] "
                if tag_id:
                    tag_ids.append(tag_id)
                    attempt_log += f"ID: {tag_id}"
                else:
                    attempt_log += "-- タグを検出できませんでした --"
                
                read_attempts.append(attempt_log)
                self.logs.append(attempt_log)
                
                # 次の読み取りまでの待機時間を削減
                if i < count - 1:  # 最後の読み取りでは待機しない
                    time.sleep(0.005)  # 0.01から0.005に短縮
            
            # 最も多く検出されたIDを返す
            if tag_ids:
                tag_counter = Counter(tag_ids)
                most_common_tag = tag_counter.most_common(1)[0]
                result_log = f"Most common tag: {most_common_tag[0]} (detected {most_common_tag[1]} times)"
                logger.info(result_log)
                self.logs.append(result_log)
                return most_common_tag[0], read_attempts
            else:
                no_tag_log = "No tags detected in any attempts"
                logger.warning(no_tag_log)
                self.logs.append(no_tag_log)
                return None, read_attempts
                
        finally:
            self.disconnect()

# グローバルなRFIDリーダーインスタンス
rfid_reader = None

def get_rfid_reader():
    """RFIDリーダーのシングルトンインスタンスを取得"""
    global rfid_reader
    if rfid_reader is None:
        rfid_reader = RFIDReader()
    return rfid_reader

@csrf_exempt
@require_http_methods(["POST"])
def read_rfid_api(request):
    """RFID読み取りAPI"""
    try:
        # リクエストから読み取り回数を取得（デフォルト3回）
        data = json.loads(request.body) if request.body else {}
        read_count = data.get('count', 3)
        
        reader = get_rfid_reader()
        most_common_tag, read_attempts = reader.read_multiple_tags(read_count)
        
        return JsonResponse({
            'success': True,
            'tag_id': most_common_tag,
            'message': f'RFID読み取り完了 ({read_count}回)' if most_common_tag else 'タグが検出されませんでした',
            'read_attempts': read_attempts,
            'logs': reader.logs[-20:]  # 最新の20件のログ
        })
    except Exception as e:
        error_msg = f'RFID読み取りエラー: {str(e)}'
        logger.error(error_msg)
        return JsonResponse({
            'success': False,
            'message': error_msg,
            'tag_id': None,
            'logs': [error_msg]
        }, status=500)

@require_http_methods(["GET"])
def rfid_status_api(request):
    """RFID読み取り状況を取得するAPI"""
    try:
        reader = get_rfid_reader()
        return JsonResponse({
            'success': True,
            'status': {
                'port': reader.port,
                'baud_rate': reader.baud_rate,
                'connected': reader.ser.is_open if reader.ser else False
            },
            'logs': reader.logs[-10:]  # 最新の10件のログ
        })
    except Exception as e:
        error_msg = f'RFID状況取得エラー: {str(e)}'
        return JsonResponse({
            'success': False,
            'message': error_msg,
            'logs': [error_msg]
        }, status=500)
