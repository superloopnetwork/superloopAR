from parser import parser
from multithread import multithread_engine
import subprocess
import re

def main():

	syslog = []
	refresh = True

	while True:

		tail = subprocess.Popen('tail -f -n 0 /mnt/syslog/**/*.log', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
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
				tail.kill()
				refresh = False

if __name__ == '__main__':
	main()
