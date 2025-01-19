import cv2
import numpy as np


balls	= cv2.imread('sport.jpg')
gray_img	=	cv2.cvtColor(balls,	cv2.COLOR_BGR2GRAY)
img	= cv2.medianBlur(gray_img,	5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#center

circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
circles	= np.uint16(np.around(circles))

for	i in circles[0,:]:
				#	draw	the	outer	circle
				cv2.circle(balls,(i[0],i[1]),i[2],(0,255,0),6)
				#	draw	the	center	of	the	circle
				cv2.circle(balls,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("HoughCirlces",	balls)
cv2.waitKey()
cv2.destroyAllWindows()