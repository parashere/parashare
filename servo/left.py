from gpiozero import Servo
from time import sleep

servo = Servo(pin=13)

print(f"value=(val=1.0)")
servo.value = 1.0
sleep(2)
