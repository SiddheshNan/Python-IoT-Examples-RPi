import serial,time

usb2 = '/dev/ttyUSB1'
ser2 = serial.Serial(usb2, 9600)

while True:

	out=ser2.readline().decode()

	print("Recived data : " + str(out))
