import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api
from ctypes import windll # for dpi awareness to fix cursor wrong position issue under high dpi scaling
import os
from screengrab import grab_screen

windll.user32.SetProcessDPIAware()
last_time = time.time()

lower_red = np.array([120,50,100])
upper_red = np.array([255,255,255])

def nothing(x):
	pass
cv2.namedWindow("Trackbars",cv2.WINDOW_NORMAL)
cv2.createTrackbar("L - H", "Trackbars", 0,255, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0,255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0,255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 0,255, nothing)
cv2.createTrackbar("U - S", "Trackbars", 0,255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 0,255, nothing)



while(True):
	x,y = win32api.GetCursorPos()
	x,y = 3840//2 , 2160//2
	sscreen = np.array(grab_screen([x-250,y-250,x+250,y+250]))

	lh = cv2.getTrackbarPos("L - H", "Trackbars")
	ls = cv2.getTrackbarPos("L - S", "Trackbars")
	lv = cv2.getTrackbarPos("L - V", "Trackbars")
	uh = cv2.getTrackbarPos("U - H", "Trackbars")
	us = cv2.getTrackbarPos("U - S", "Trackbars")
	uv = cv2.getTrackbarPos("U - V", "Trackbars")

	lower_bound = np.array([lh,ls,lv])
	upper_bound = np.array([uh,us,uv])
	hsv = cv2.cvtColor(sscreen, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_bound, upper_bound)

	last_time = time.time()
	


	# screengrab = ImageGrab.grab(bbox = (x-250,y-250,x+250,y+250))
	# printscreen_numpy= np.array(printscreen_pil.getdata(), dtype = 'uint8').reshape( (printscreen_pil.size[1],printscreen_pil.size[0],3))
	
	
	


	result = cv2.bitwise_and(cv2.cvtColor( sscreen,cv2.COLOR_BGR2RGB),cv2.cvtColor( sscreen,cv2.COLOR_BGR2RGB),mask=mask)
	cv2.imshow('screen capture',cv2.cvtColor( sscreen,cv2.COLOR_BGR2RGB))
	cv2.imshow("mask",mask)
	cv2.imshow('result',result)

	#final = cv2.bitwise_and(sscreen,mask, mask )
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break

	print("time update : {} seconds".format(time.time() - last_time))