import Adafruit_DHT
from Adafruit_CharLCD import Adafruit_CharLCD
import time
hum,temp=Adafruit_DHT.read_retry(11,2)
lcd = Adafruit_CharLCD()
lcd.clear()
lcd.begin(16, 2)
lcd.setCursor(1, 0)
lcd.message(str(hum))
lcd.message(str(temp))
lcd.display()

