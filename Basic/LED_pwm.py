import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
p=GPIO.PWM(2,50)
p.start(0)

while True:
	for i in range(0,10):
		p.ChangeDutyCycle(i)
		time.sleep(1)
		print("Brighter")

	for i in range(10,0,-1):
		p.ChangeDutyCycle(i)
		time.sleep(1)
		print("Lighter")
