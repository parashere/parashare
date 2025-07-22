from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
factory = PiGPIOFactory()
servo = Servo(13, pin_factory=factory)  # GPIO13に接続
print("value=(val=1.0)")
servo.value = 1.0  # 最大位置
sleep(2)
