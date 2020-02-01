import serial
import time
usbport = '/dev/ttyUSB0'
ser = serial.Serial(usbport, 9600)
while True:
	data = input("input data")
	ser.write((data + '\r\n').encode())


