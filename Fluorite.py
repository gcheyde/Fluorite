import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pins = [] #add pin numbers once we figure them out
for i in pins:
    GPIO.setup(i, GPIO.OUT)
p = GPIO.PWM(,0) #pin numbers to be figured out later
w = GPIO.PWM(,0)
m = GPIO.PWM(,0)
for i in range(100):
    for i in range(100):
        p.ChangeDutyCycle(,i)
        w.ChangeDutyCycle(,(i+33)%100)
        m.ChangeDutyCycle(,(i+33)%100)
        sleep(0.1)
#motor 1
GPIO.setup(,GPIO.OUT) #A1
GPIO.setup(,GPIO.OUT) #A2
GPIO.setup(,GPIO.OUT) #B1
GPIO.setup(,GPIO.OUT) #B2
GPIO.setup(,GPIO.OUT) #sleep
p1 = GPIO.PWM(,50) #A1
ppp1 = GPIO.PWM(,50) #A2
pp1 = GPIO.PWM(,50) #B1
pppp1 = GPIO.PWM(,50) #B2
GPIO.output(,GPIO.HIGH)
p1.start(0)
pp1.start(0)
ppp1.start(0)
pppp1.start(0)
#motor 2
GPIO.setup(,GPIO.OUT) #A1
GPIO.setup(,GPIO.OUT) #A2
GPIO.setup(,GPIO.OUT) #B1
GPIO.setup(,GPIO.OUT) #B2
GPIO.setup(,GPIO.OUT) #sleep
p2 = GPIO.PWM(,50) #A1
ppp2 = GPIO.PWM(,50) #A2
pp2 = GPIO.PWM(,50) #B1
pppp2 = GPIO.PWM(,50) #B2
GPIO.output(,GPIO.HIGH)
p2.start(0)
pp2.start(0)
ppp2.start(0)
pppp2.start(0)

for i in range(150):
    p1.ChangeDutyCycle(100) #1000
    p2.ChangeDutyCycle(100) #1000
    sleep(0.01)
    pp1.ChangeDutyCycle(100) #1100
    pp2.ChangeDutyCycle(100) #1100
    sleep(0.01)
    p1.ChangeDutyCycle(0) #0100
    p2.ChangeDutyCycle(0) #0100
    sleep(0.01)
    ppp1.ChangeDutyCycle(100) #0110
    ppp2.ChangeDutyCycle(100) #0110
    sleep(0.01)
    pp1.ChangeDutyCycle(0) #0010
    pp2.ChangeDutyCycle(0) #0010
    sleep(0.01)
    pppp1.ChangeDutyCycle(100) #0011
    pppp2.ChangeDutyCycle(100) #0011
    sleep(0.01)
    ppp1.ChangeDutyCycle(0) #0001
    ppp2.ChangeDutyCycle(0) #0001
    sleep(0.01)
    p1.ChangeDutyCycle(100) #1001
    p2.ChangeDutyCycle(100) #1001
    sleep(0.01)
    pppp1.ChangeDutyCycle(0) #1000
    pppp2.ChangeDutyCycle(0) #1000
    sleep(0.01)

p.stop()
w.stop()
m.stop()
GPIO.cleanup()
