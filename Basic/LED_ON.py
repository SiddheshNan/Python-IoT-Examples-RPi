import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led=2
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,1)
