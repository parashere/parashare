import serial
import time

def read_single_tag(ser):
    """リーダーに1回だけ読み取り命令を送り、応答を返す関数"""
    try:
        # コマンドを送信
        command_to_send = bytes([0x7C, 0xFF, 0xFF, 0x20, 0x00, 0x00, 0x66])
        ser.write(command_to_send)
        
        # 応答を待つ
        time.sleep(0.1)
        response = ser.read(128)
        
        if response and response.startswith(b'\xCC\xFF\xFF\x20\x02'):
            epc_start_index = 10
            epc_length = 12
            epc_end_index = epc_start_index + epc_length
            if len(response) >= epc_end_index:
                epc = response[epc_start_index:epc_end_index]
                return epc.hex().upper()
    except Exception:
        return None
    return None

def main():
    SERIAL_PORT = '/dev/ttyACM0'  # Raspberry Pi用のシリアルポート
    BAUD_RATE = 115200
    
    ser = None
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        print(f"ポート {SERIAL_PORT} を開きました。10回読み取ります...")
        
        # 10回ループして読み取りを実行
        for i in range(10):
            tag_id = read_single_tag(ser)
            if tag_id:
                print(f"[{i+1:2d}回目] ID: {tag_id}")
            else:
                print(f"[{i+1:2d}回目] -- タグを検出できませんでした --")
            
            # 次の読み取りまで少し待つ
            time.sleep(0.01)

    except serial.SerialException as e:
        print(f"エラー: ポートを開けませんでした。 {e}")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("ポートを閉じました。")

if __name__ == '__main__':
    main()