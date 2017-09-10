####################### ENGINE FUNCTIONS ########################

from parser import parser
import threading
import time
import datetime

def multithread_engine(object):
	print object[0]	
	start_time = datetime.datetime.now()
	index = 0

	for i in object:
		my_thread = threading.Thread(target=parser, args=(i,))
		my_thread.start()

		index = index + 1

	main_thread = threading.currentThread()
	for some_thread in threading.enumerate():
		if some_thread != main_thread:
			print(some_thread)
			some_thread.join()

