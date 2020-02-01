import serial

usb1 = '/dev/ttyUSB0'
ser1 = serial.Serial(usb1, 9600)

usb2 = '/dev/ttyUSB1'
ser2 = serial.Serial(usb2, 9600)

while True:
	in1 = input("input data : ")

	ser1.write((in1+'\r\n').encode())

	out=ser2.readline().decode()

	print("Recived data : " + str(out))
