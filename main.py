from parser import parser
from multithread import multithread_engine
import subprocess
import re

def main():

	syslog = []
	index = 0

	tail = subprocess.Popen('tail -f -n 1 /mnt/syslog/**/*.log', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

	while True:
		line = tail.stdout.readline()
		line = line.strip('\n')
		if(re.search('mnt',line)) or (line == ''):
			pass	
		else:
			syslog.append(line)
			multithread_engine(syslog)
			del syslog[:]

if __name__ == '__main__':
	main()
