from Adafruit_CharLCD import Adafruit_CharLCD
import time


#Getting the instance of the lib
lcd = Adafruit_CharLCD()
lcd.clear()
#Input from user
msg = raw_input("Enter message to display\n")
lcd.setCursor(1, 4)
#Display it on the LCD
lcd.message(str(msg))

#You can use other functions in the library

#Clearing the display
#lcd.clear()

#Toggle the text visibility on the LCD
#lcd.noDisplay()  #Make the text invisible
#lcd.display()    #Make the text visible

#Toggle cursor visibility
#lcd.noCursor()   	#Make the cursor invisible
#lcd.cursor()     	#Make the cursor visible

#Blink the cursor
#lcd.noBlink()    	#Disable the cursor blink
#lcd.blink()	  	#Make the cursor blink

#Position the cursor to the start of the display
#lcd.home()

#Position the cursor to a specific location on the display
#Before setting the position, set the number of columns and rows like so
#lcd.begin(16,2)	#As I am using 16x2 LCD
#lcd.setCursor(12, 1)	#Positions the cursor at 11th column in 2nd row
