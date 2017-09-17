from parser import parser
from multithread import multithread_engine
import subprocess
import re

def main():

	syslog = []
	refresh = True
	purge = True
	history = []

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
			
			if(re.search('mnt',line) or line == ''): 
				pass
			
			else:
				if(line in history):
					pass
				else:
					syslog.append(line)
					if(len(history)<=50):
						history.append(line)
					elif(len(history)>50):
						history.pop(0)
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
