from Adafruit_CharLCD import Adafruit_CharLCD
lcd=Adafruit_CharLCD()
lcd.begin(16,2)
lcd.setCursor(1,1)
lcd.clear()
lcd.message('welcome')
print "hello"
