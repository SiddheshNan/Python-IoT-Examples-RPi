import serial,time

usb1 = '/dev/ttyUSB1'
ser1 = serial.Serial(usb1, 9600)

usb2 = '/dev/ttyAMA0'
ser2 = serial.Serial(usb2, 9600)

while True:
	input = input("input data : ")

	ser1.write((input+'\r\n').encode())

	output=ser2.readline().decode()

	print("Recived data : " + str(output))
