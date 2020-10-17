from gpiozero import Servo, LED
from time import sleep
from slow import sweep

#pins 23 and 24 connect to servos w signal wire
tilt = Servo(24)
pan = Servo(23)
l_led = LED(22)
r_led = LED(17)

#initial tilt to minimum pos (horizontal)
#inital pan to middle pos (straight)
tilt.value = -1
pan.value = 0
#after any position adjustment allow small wait for servo to respond before detachment
sleep(0.3)
tilt.detach()
pan.detach()
sleep(1)
print('Left LED On')
l_led.on()
sleep(2)
print('Left LED Off')
l_led.off()
sleep(1)
print('Right LED On')
r_led.on()
sleep(2)
print('Right LED Off')
r_led.off()
sleep(1)
print(3)
sleep(2)
print(2)
sleep(2)
print(1)
sleep(2)
print('Initialized')
sleep(1)
c = 0

while c <2:
    yt = sweep(pan,0,1,10)
    sleep(2)
    yt = sweep(pan,yt,-1,10)
    sleep(2)
    yt = sweep(pan,yt,0,10)
    sleep(2)
    
    xt = sweep(tilt,-1,1,10)
    sleep(2)
    
    yt = sweep(pan,yt,1,10)
    sleep(2)
    yt = sweep(pan,yt,-1,10)
    sleep(2)
    yt = sweep(pan,yt,0,10)
    sleep(2)
    
    xt = sweep(tilt,xt,0,10)
    sleep(2)
    
    yt = sweep(pan,yt,1,10)
    sleep(2)
    yt = sweep(pan,yt,-1,10)
    sleep(2)
    yt = sweep(pan,yt,0,10)
    sleep(2)
    
    xt = sweep(tilt,xt,-1,10)
    sleep(2)
    
    c += 1

tilt.min()
sleep(.3)
tilt.detach()
sleep(0.7)

