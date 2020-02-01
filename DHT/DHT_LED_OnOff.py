import RPi.GPIO as GPIO
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led1=3
GPIO.setup(led1,GPIO.OUT)
GPIO.output(led1,0)

hum,temp=Adafruit_DHT.read_retry(11,2)
print(hum,temp)

if(temp>25):
	GPIO.output(led1,1)
