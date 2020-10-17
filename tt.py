from gpiozero import LED, Servo
from time import sleep

led = LED(17)
servo = Servo(23, initial_value = -1)
sleep(1)
# led.on()
# sleep(.1)
# led.off()
# servo.mid()
# sleep(0.3)
print(servo.value)
servo.detach()