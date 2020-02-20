import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api , win32con, win32gui, winsound
from ctypes import windll # for dpi awareness to fix cursor wrong position issue under high dpi scaling
import os
from screengrab import grab_screen



windll.user32.SetProcessDPIAware()



#first create trainning data folder, if trainning data folder already exists, skip
def folder_creation(path):	
	if os.path.exists(path):
		print("folder exist, skip creation for " + path)
	else:
		print("making new directory for " + path)
		os.mkdir(path)

folder_creation("ClassifiedData")
folder_creation("ClassifiedData/hit")
folder_creation("ClassifiedData/miss")


while(True):
	
	Lmouse = win32api.GetAsyncKeyState((win32con.VK_LBUTTON))
	Ctrl = win32api.GetAsyncKeyState((win32con.VK_CONTROL))
	Shift = win32api.GetAsyncKeyState((win32con.VK_SHIFT))

	x,y = win32api.GetCursorPos()

	print(x,y)
	screengrab = grab_screen([x-250,y-250,x+250,y+250])
	# printscreen_numpy= np.array(printscreen_pil.getdata(), dtype = 'uint8').reshape( (printscreen_pil.size[1],printscreen_pil.size[0],3))
	
	
	
	cv2.imshow('screen capture',cv2.cvtColor( np.array(screengrab),cv2.COLOR_BGR2RGB))

	last_time = time.time()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
	print("time update : {} seconds".format(time.time() - last_time))

	print(str(Lmouse) + "  " + str(Ctrl) + " " + str(Shift))

	if( Shift != 0):
		cv2.imwrite("ClassifiedData/hit/"+str(time.time())+".png",cv2.cvtColor( np.array(screengrab),cv2.COLOR_BGR2RGB))
	elif (Ctrl != 0):
		cv2.imwrite("ClassifiedData/miss/"+str(time.time())+".png",cv2.cvtColor( np.array(screengrab),cv2.COLOR_BGR2RGB))
