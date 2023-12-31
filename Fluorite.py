import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pins = [23,24,25,8,7,12,26] #LED pins
for i in pins:
    GPIO.setup(i, GPIO.OUT)
p = GPIO.PWM(23,100) #setting up PWM
w = GPIO.PWM(24,100)
m = GPIO.PWM(25,100)
pp = GPIO.PWM(8,100)
ww = GPIO.PWM(7,100)
mm = GPIO.PWM(12,100)
ppp = GPIO.PWM(26,100)
p.start(0)
w.start(0)
m.start(0)
pp.start(0)
ww.start(0)
mm.start(0)
ppp.start(0)
#motor 1
GPIO.setup(16,GPIO.OUT) #A1
GPIO.setup(17,GPIO.OUT) #A2
GPIO.setup(19,GPIO.OUT) #B1
GPIO.setup(18,GPIO.OUT) #B2
GPIO.setup(3,GPIO.OUT) #sleep
p1 = GPIO.PWM(16,50) #A1
ppp1 = GPIO.PWM(17,50) #A2
pp1 = GPIO.PWM(19,50) #B1
pppp1 = GPIO.PWM(18,50) #B2
GPIO.output(3,GPIO.HIGH)
p1.start(0)
pp1.start(0)
ppp1.start(0)
pppp1.start(0)
#motor 2
GPIO.setup(13,GPIO.OUT) #A1
GPIO.setup(6,GPIO.OUT) #A2
GPIO.setup(4,GPIO.OUT) #B1
GPIO.setup(5,GPIO.OUT) #B2
GPIO.setup(2,GPIO.OUT) #sleep
p2 = GPIO.PWM(13,50) #A1
ppp2 = GPIO.PWM(6,50) #A2
pp2 = GPIO.PWM(4,50) #B1
pppp2 = GPIO.PWM(5,50) #B2
GPIO.output(2,GPIO.HIGH)
p2.start(0)
pp2.start(0)
ppp2.start(0)
pppp2.start(0)
#running the motors and changing the LEDs at the same time
for i in range(10000):
    p.ChangeDutyCycle((i*4)%70)
    w.ChangeDutyCycle(((i*4+20))%70)
    m.ChangeDutyCycle(((i*4+40))%70)
    pp.ChangeDutyCycle((i*4)%70)
    ww.ChangeDutyCycle(((i*4+20))%70)
    mm.ChangeDutyCycle(((i*4+40))%70)
    ppp.ChangeDutyCycle((i*4)%70)
    p1.ChangeDutyCycle(100) #1000
    p2.ChangeDutyCycle(100) #1000
    sleep(0.02)
    pp1.ChangeDutyCycle(100) #1100
    pp2.ChangeDutyCycle(100) #1100
    sleep(0.02)
    p1.ChangeDutyCycle(0) #0100
    p2.ChangeDutyCycle(0) #0100
    sleep(0.02)
    ppp1.ChangeDutyCycle(100) #0110
    ppp2.ChangeDutyCycle(100) #0110
    sleep(0.02)
    pp1.ChangeDutyCycle(0) #0010
    pp2.ChangeDutyCycle(0) #0010
    sleep(0.02)
    pppp1.ChangeDutyCycle(100) #0011
    pppp2.ChangeDutyCycle(100) #0011
    sleep(0.02)
    ppp1.ChangeDutyCycle(0) #0001
    ppp2.ChangeDutyCycle(0) #0001
    sleep(0.02)
    p1.ChangeDutyCycle(100) #1001
    p2.ChangeDutyCycle(100) #1001
    sleep(0.02)
    pppp1.ChangeDutyCycle(0) #1000
    pppp2.ChangeDutyCycle(0) #1000
    sleep(0.02)

p.stop()
w.stop()
m.stop()
pp.stop()
ww.stop()
mm.stop()
ppp.stop()
p1.stop()
pp1.stop()
ppp1.stop()
pppp1.stop()
p2.stop()
pp2.stop()
ppp2.stop()
pppp2.stop()
GPIO.cleanup()
