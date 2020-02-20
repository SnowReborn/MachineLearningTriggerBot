import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api
from ctypes import windll # for dpi awareness to fix cursor wrong position issue under high dpi scaling
import os

windll.user32.SetProcessDPIAware()
time.sleep(5)
last_time = time.time()

#first create trainning data folder, if trainning data folder already exists, skip
if os.path.exists("TrainningDataFolder"):
	print("Trainning data exists, skipping creation")
else:
	print("making new directory")
	os.mkdir("TrainningDataFolder")
counter = 3 # taking picture per 100 second

while(True):
	
	x,y = win32api.GetCursorPos()

	print(x,y)
	screengrab = ImageGrab.grab(bbox = (x-250,y-250,x+250,y+250))
	# printscreen_numpy= np.array(printscreen_pil.getdata(), dtype = 'uint8').reshape( (printscreen_pil.size[1],printscreen_pil.size[0],3))
	
	print("time update : {} seconds".format(time.time() - last_time))
	last_time = time.time()
	#cv2.imshow('screen capture',cv2.cvtColor( np.array(screengrab),cv2.COLOR_BGR2RGB))
	counter -= 1
	print("COUNTER :  " + str(counter))


	if counter < 0:
		cv2.imwrite("TrainningDataFolder/"+str(time.time())+".png",cv2.cvtColor( np.array(screengrab),cv2.COLOR_BGR2RGB))
		counter = 3
