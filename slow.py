from gpiozero import Servo
from time import sleep

def sweep(servo,x,y,div): #Where x is initial position (-1,1) and div is step size
    #servo is servo object
    
    current_position = x
    displacement = y - current_position
    step = displacement/div
    
    for i in range(div):
        current_position = current_position + step
        servo.value = current_position
        sleep(0.01)
    servo.detach()
    
    return y
    