import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
led1=2
led2=17
led3=18
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.output(led1,0)
GPIO.output(led2,0)
GPIO.output(led3,0)
while True:
	GPIO.output(led1,1)
	time.sleep(4)
	GPIO.output(led1,0)
	GPIO.output(led2,1)
	time.sleep(2)
	GPIO.output(led2,0)
	GPIO.output(led3,1)
	time.sleep(4)
	GPIO.output(led3,0)
