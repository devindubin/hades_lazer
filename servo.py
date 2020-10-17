from gpiozero import Servo, LED
import random, time, traceback

def Main():
    try:
        
        r_led = LED(17)
        l_led = LED(22)
        """Pan/Tilt Pins"""
        pan = Servo(24, initial_value = 0) #breakout pin 18
        tilt = Servo(23,initial_value = -1) #breakout pin 16
        time.sleep(0.2)
        
        
        pan.detach()
        tilt.detach()
        c = 0
        print('initializing')
        time.sleep(5)
        
        r_led.on()
        while c < 5:
            
            
            alpha_pan = random.uniform(-1,1)
            alpha_tilt = random.uniform(-1,-0.5)
            
            print('random nums made')
            print(alpha_pan,alpha_tilt)
            time.sleep(1)

            pan.value = alpha_pan
            time.sleep(0.3)
            pan.detach()
            time.sleep(1)
            r_led.off()
            print('move pan')
            time.sleep(3)

            
            tilt.value = alpha_tilt
            time.sleep(0.3)
            tilt.detach()
            time.sleep(1)
            
            
            print('move tilt')
            time.sleep(3)
            #GPIO.output(3,GPIO.LOW)
            c += 1


        
            

        


    except Exception as ex:
        traceback.print_exc()
    finally:
        #tilt.stop()
        #pan.stop()
        #GPIO.cleanup()
        pan.value = 0
        tilt.value = -1
        time.sleep(0.3)
        pan.detach()
        tilt.detach()
        print('Done')
        

Main()