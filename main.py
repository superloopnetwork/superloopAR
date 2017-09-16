from parser import parser
from multithread import multithread_engine
import subprocess
import re

def main():

	syslog = []
	refresh = True

	while True:

		tail = subprocess.Popen('tail -f -n 0 /mnt/syslog/**/*.log', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		before_count = int(ls())
		refresh = True
		
		while refresh:
			line = tail.stdout.readline()
			line = line.strip('\n')
			
			if(re.search('mnt',line) or line == ''): 
				pass
			
			else:
				syslog.append(line)
				multithread_engine(syslog)
				del syslog[:]
				current_count = int(ls())
				print 'Before Count: %s' % before_count
				print 'Current Count: %s' % current_count
				if(current_count > before_count):
					tail.kill()
					refresh = False

def ls():

	ls = subprocess.Popen('ls /mnt/syslog/**/*.log | wc -l', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	list = ls.stdout.readline()
	list = list.strip('\n')
	devcount = int(list)
	ls.kill()

	return devcount

if __name__ == '__main__':
	main()
