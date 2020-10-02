from gpiozero.pins.mock import MockPWMPin, MockFactory
from gpiozero import Servo, Device
from time import sleep
import random

Device.pin_factory = MockFactory()


red = MockPWMPin(Device.pin_factory,18)

"""GPIO Servo documentation"""
#servo_pin_pan = Device.pin_factory.pin(18)
pan_servo = Servo(red)

# #Hardware sourced PWM pins: 12,13,18,19




# pan_servo = gpiozero.Servo(pin18)
# tilt_servo = gpiozero.Servo(pin19)

