#!/usr/bin/env python

from parser import parser
from multithread import multithread_engine
import lib.globalvar
import subprocess
import re

def main():

	syslog = []
	refresh = True
	purge = True
	history = []
	lib.globalvar.variables()

	while True:
		if(purge):
			tail = subprocess.Popen('tail -f -n 0 /mnt/syslog/**/*.log', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			before_count = int(ls())
		
		else:
			tail = subprocess.Popen('tail -f -n 20 /mnt/syslog/**/*.log', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			before_count = int(ls())


		refresh = True
		
		while refresh:
			line = tail.stdout.readline()
			line = line.strip('\n')
			current_count = int(ls())
			if(current_count > before_count):
				tail.kill()
				purge = False
				refresh = False

			### IF THE OUTPUT FROM THE TAIL HAS 'mnt' OR '', DO NOTHING (DON'T PROCESS)	
			if(re.search('mnt',line) or line == ''): 
				pass
	
			### START THE PROCESSING OF THE LOG LINES 
			else:

				### IF THE LINE ALREADY EXISTS IN HISTORY, DO NOTHING (DON'T PROCESS). THIS IS TO ACCOMODATE ANY RE-TAILING FROM HAPPENING.
				if(line in history):
					pass
				else:

					### APPEND THE OUTPUT LOG ENTRY ONTO THE SYSLOG LIST VARIABLE
					syslog.append(line)

					### HISTORY LIST ACTS AS A BUFFER. MAX SIZE = 1000
					if(len(history)<=1000):
						history.append(line)

					### WHEN THE LENGTH OF HISTORY EXCEEDS 1000, POP OFF THE FIRST ENTRY
					elif(len(history)>1000):
						history.pop(0)

					### START THE PROCESSING OF SYSTEM VIA MULTITHREAD
					multithread_engine(syslog)
					del syslog[:]

def ls():

	ls = subprocess.Popen('ls /mnt/syslog/**/*.log | wc -l', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	list = ls.stdout.readline()
	list = list.strip('\n')
	devcount = int(list)
	ls.kill()

	return devcount

if __name__ == '__main__':
	main()
