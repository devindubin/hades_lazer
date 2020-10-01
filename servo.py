from gpiozero.pins.mock import MockPWMPin, MockFactory
import gpiozero
import time
import random




"""GPIO Servo documentation"""
# gpiozero.Servo(pin, *, initial_value=0, 
# min_pulse_width=1/1000, max_pulse_width=2/1000, 
# frame_width=20/1000, pin_factory=None)

#Hardware sourced PWM pins: 12,13,19
# pin18 = gpiozero.Device.pin_factory.pin(18) # pan_servo pin
# pin19 = gpiozero.Device.pin_factory.pin(19) # tilt_servo pin

pin18 = MockPWMPin(MockFactory,18) # pan_servo pin
pin19 = MockPWMPin(19)

pan_servo = gpiozero.Servo(pin18)
tilt_servo = gpiozero.Servo(pin19)

