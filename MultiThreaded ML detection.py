from threading import Thread
from multiprocessing import Process
import time



result = 3

def returnone():
	while True:
		global result
		result += 1
		time.sleep(0.1)

		


def addthree():
	while True:
		global result
		print('result is : ', result)
		time.sleep(0.1)

def minusone():
	global result
	while True:
		if result > -500:
			result -= 5
			time.sleep(0.1)
		
t1 = Thread(target=returnone)
t2 = Thread(target=addthree)
t3 = Thread(target=minusone)


t1.start()
# time.sleep(5)

t2.start()
t3.start()





# from threading import Thread
# import time
# a = 0  #global variable

# def thread1(threadname):
#     #global a       # Optional if you treat a as read-only
#     while True:
#         print(a)
# def thread2(threadname):
#     global a
#     while True:
#         a += 1
#         time.sleep(0.01)
        
# thread1 = Thread( target=thread1, args=("Thread-1", ) )
# thread2 = Thread( target=thread2, args=("Thread-2", ) )
# thread1.start()
# thread2.start()