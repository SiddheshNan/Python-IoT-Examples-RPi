import serial
usb = '/dev/ttyAMA0'
ser = serial.Serial(usb, 9600)
while True:
	mes=ser.readline().decode()
	print (str(mes))
