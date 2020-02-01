import cv2
import imutils
from mailgun import mail

webcam = cv2.VideoCapture(0)

while True:
	_, im = webcam.read()
	im = imutils.resize(im, width=400)
	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break
	if key & 0xFF == ord('c'):	
		print ('sending mail...')
		cv2.imwrite('img_file.jpg',im)
		mail('mail@example.com', 'Attendance Management',
                 'Attendace taken for the day ', 'img_file.jpg')
	cv2.imshow('OpenCV', im)
