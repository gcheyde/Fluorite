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
p.stop()
w.stop()
m.stop()
GPIO.cleanup()
