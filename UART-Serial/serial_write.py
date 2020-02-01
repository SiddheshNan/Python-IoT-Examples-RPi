import serial

usb = '/dev/ttyUSB1'

ser1 = serial.Serial(usb, 9600)

while True:
	data1 = input("input data : ")

	ser1.write((data1+'\r\n').encode())
