from EmulatorGUI import GPIO
from gpiozero import Servo
import random, time, traceback

def Main():
    try:

        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)
        
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(19,GPIO.OUT)
        GPIO.setup(4,GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(2,GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(3,GPIO.OUT, initial = GPIO.LOW)


        """Pan/Tilt Pins"""
        # pan = GPIO.PWM(18,50)
        # tilt = GPIO.PWM(19,50)

        """Start both servos at 0 Duty Cycle"""
        # pan.start(0)
        # tilt.start(0)
        """Counter"""
        c = 0
        while c < 5:
            GPIO.output(4,GPIO.HIGH)
            
            alpha_pan = random.randint(0,180)
            alpha_tilt = random.randint(0,180)
            dc_pan = (alpha_pan/18) + 3
            dc_tilt = (alpha_tilt/18) + 3

            time.sleep(2)

            GPIO.output(4,GPIO.LOW)
            #pan.ChangeDutyCycle(dc_pan)
            GPIO.output(2,GPIO.HIGH)

            time.sleep(2)

            GPIO.output(2,GPIO.LOW)
            #tilt.ChangeDutyCycle(dc_tilt)
            GPIO.output(3,GPIO.HIGH)

            time.sleep(2)
            GPIO.output(3,GPIO.LOW)
            c += 1


        #tilt.stop()
        #pan.stop()
            

        


    except Exception as ex:
        traceback.print_exc()
    finally:
        
        GPIO.cleanup()

Main()