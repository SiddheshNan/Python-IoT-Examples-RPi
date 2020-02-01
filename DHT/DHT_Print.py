import Adafruit_DHT
import time

while True:
    hum,temp=Adafruit_DHT.read_retry(11,2)
    print(hum,temp)
    time.sleep(1)
