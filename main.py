from parser import parser
from multithread import multithread_engine
import subprocess
import re

def main():

	syslog = []

	tail = subprocess.Popen('tail -f -n 1 /mnt/syslog/**/*.log', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	database = []
	
	while True:
		line = tail.stdout.readline()
		line = line.strip('\n')
		
		if(re.search('mnt',line)): 
			if(not database):
				database.append(line)
				purge = True
			elif(line in database):
				print 'IN DATABASE: %s' % line
				purge = False
			else:
				database.append(line)
				purge = True
			
		elif(line == ''):
			pass
		
		elif(purge):
			purge = False
			pass
		
		else:
			syslog.append(line)
			multithread_engine(syslog)
			del syslog[:]

if __name__ == '__main__':
	main()
