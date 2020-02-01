from Adafruit_CharLCD import Adafruit_CharLCD
import Adafruit_DHT
import time
lcd = Adafruit_CharLCD()

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11,2)
	lcd.begin(16, 2)
	lcd.setCursor(0, 1)
	lcd.message("humidity :")
	lcd.setCursor(10,1)
	lcd.message(str(humidity))
	lcd.setCursor(0,0)
	lcd.message("temp :")
	lcd.setCursor(7, 0)
	lcd.message(str(temperature))
	time.sleep(2)
	lcd.clear()

