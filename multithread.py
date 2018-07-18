####################### ENGINE FUNCTIONS ########################

### AN OBJECT IS CREATED FOR EACH EVENT OR SYSLOG ENTRY OUTPUT

from parser import parser
import threading
import time
import datetime

def multithread_engine(object):

	start_time = datetime.datetime.now()

	for i in object:
		my_thread = threading.Thread(target=parser, args=(i,))
		my_thread.start()

	main_thread = threading.currentThread()
	for some_thread in threading.enumerate():
		if some_thread != main_thread:
			print(some_thread)
			some_thread.join()

