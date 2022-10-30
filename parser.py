####################### ENGINE FUNCTIONS ########################
from event import event
import re

def parser(syslog_line):

	COLUMN_DELIMITER_RE = r'(\s+)'
	DEVICE_IP_RE = r'(\d+\.\d+\.\d+\.\d+)'
	DATESTAMP_RE = r'(.+?\s+\d+)'
	ERROR_CODE_RE = r'%(\S+):'
	ERROR_MESSAGE_RE = r'(.*)'
	INTERFACE_RE = r'(\w+\d+\/\d+)'
	HOSTNAME_RE = r'(\S+)'
	TIMESTAMP_RE = r'(\d+:\d+:\d+.\d+)'
	USER_ID_RE = r'by\s(\w+\.\w+)\s'
	
	dstamp = re.search(DATESTAMP_RE, syslog_line).group(1)
	tstamp = re.search(TIMESTAMP_RE, syslog_line).group(1)
	device = re.search(DEVICE_IP_RE, syslog_line).group(1)
	error_code = re.search(ERROR_CODE_RE, syslog_line).group(1)
	error_message = re.search(ERROR_MESSAGE_RE, syslog_line).group(1)

	ntw_device = get_ntw_device(device)

	event(dstamp,tstamp,device,error_code,error_message,ntw_device)

def get_ntw_device(device):

	f = open('master_device_list')
	list = f.readlines()

	for element in list:
		element = element.strip('\n')
		ntw_device = element.split(',')
		if(device == ntw_device[0]):
			return ntw_device 
