from Adafruit_CharLCD import Adafruit_CharLCD
import Adafruit_DHT

lcd = Adafruit_CharLCD()

lcd.begin(16, 2)
lcd.setCursor(1, 0)

hum,temp=Adafruit_DHT.read_retry(11,2)
t = str(hum)
j = str(temp)
lcd.message("hum ={}".format(t))
lcd.setCursor(1, 1)
lcd.message("temp ={}".format(j))

