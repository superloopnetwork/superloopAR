####################### ENGINE FUNCTIONS ########################
import re

def parser(syslog_line):

	DATESTAMP_RE = r'(.+?\s+\d+)'
	TIMESTAMP_RE = r'(\d+:\d+:\d+)'
	DEVICE_IP_RE = r'(\d+\.\d+\.\d+\.\d+)'
	ERROR_CODE_RE = r':\s%*(.+?):'
	ERROR_MESSAGE_RE = r'%.+:\s(.*)'

	dstamp = re.search(DATESTAMP_RE, syslog_line).group(1)
	tstamp = re.search(TIMESTAMP_RE, syslog_line).group(1)
	device = re.search(DEVICE_IP_RE, syslog_line).group(1)
	error_c = re.search(ERROR_CODE_RE, syslog_line).group(1)
	error_m = re.search(ERROR_MESSAGE_RE, syslog_line).group(1)

	f = open('devices')
	list = f.readlines()

	for element in list:
		element = element.strip('\n')
		device_mapping = element.split(',')

	print dstamp, tstamp, device, error_c, error_m
