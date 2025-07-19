from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

servo = Servo(13)  # GPIO13に接続

print("value=(val=-1.0)")
servo.value = 1.0  # 最小位置
sleep(2)