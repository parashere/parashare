import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
print("利用可能なシリアルポート一覧:")
for port in ports:
    print(f"  {port.device} - {port.description}")