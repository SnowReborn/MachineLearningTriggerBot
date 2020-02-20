import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api
from ctypes import windll # for dpi awareness to fix cursor wrong position issue under high dpi scaling
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import win32api, win32con
from screengrab import grab_screen
from VKhotkey import press , VK_CODE
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


windll.user32.SetProcessDPIAware()

#RESTRICT VRAM


gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)

#END OF RESTRICTION

model = load_model('sample.h5',compile = False)
counterclick= 0
clicktimechecker = 0

print("Alive")

while(True):
	
	
	# x,y = win32api.GetCursorPos()


	# screengrab = 
	
	
	x, y = 3840//2 , 2160//2	
	gaa = grab_screen([x-250,y-250,x+250,y+250])

	# cv2.imshow('screen capture',cv2.cvtColor(np.array(gaa),cv2.COLOR_BGR2RGB)) # shows the window, but with RGB conversion

	# if cv2.waitKey(25) & 0xFF == ord('q'):
	# 	cv2.destroyAllWindows()
	# 	break

	



	# testing time
	cur_image = image.img_to_array(gaa)
	cur_image = np.expand_dims(cur_image,axis=0)
	# about 0.002 sec

	

	last_time = time.time()
	result = model.predict(cur_image) # version 2 takes 0.005 to 0.006
	# print("time update : {} seconds".format(time.time() - last_time))

	last_click_time = time.time() - clicktimechecker

	Shift = win32api.GetAsyncKeyState((win32con.VK_SHIFT))
	MouseB, MouseF = win32api.GetAsyncKeyState((win32con.VK_XBUTTON1)) , win32api.GetAsyncKeyState((win32con.VK_XBUTTON2)) 

	if result == 0 and (MouseF != 0) and last_click_time > 0.1:
		# print("CLICKED" + str(counterclick))
		x,y = win32api.GetCursorPos()
		click(x,y)
		print("yea boi")
		#press("ctrl") # add time clip to check so click doesn't go tooo fast 
		clicktimechecker = time.time()
		
		# print(last_click_time)
	

	

