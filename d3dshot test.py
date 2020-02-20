import d3dshot, cv2
import numpy as np
import time
d = d3dshot.create(capture_output="numpy")
while True:
	
	lasttime = time.time()

	aaa = cv2.cvtColor(d.screenshot()[0:255,0:255], cv2.COLOR_BGR2RGB)
	cv2.imshow('a',aaa)
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	print("took {} with fps : {}".format(time.time() - lasttime  , 1 / (time.time() - lasttime + 0.000001)))