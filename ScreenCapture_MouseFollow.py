import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api
from ctypes import windll # for dpi awareness to fix cursor wrong position issue under high dpi scaling
import os

windll.user32.SetProcessDPIAware()
last_time = time.time()



while(True):
	last_time = time.time()
	x,y = win32api.GetCursorPos()

	print(x,y)
	screengrab = ImageGrab.grab(bbox = (x-250,y-250,x+250,y+250))
	# printscreen_numpy= np.array(printscreen_pil.getdata(), dtype = 'uint8').reshape( (printscreen_pil.size[1],printscreen_pil.size[0],3))

	

	cv2.imshow('screen capture',cv2.cvtColor( np.array(screengrab),cv2.COLOR_BGR2RGB))
	
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break

	print("time update : {} seconds with FPS : {} ".format(time.time() - last_time ,1 / (time.time() - last_time + 0.0000000001)))