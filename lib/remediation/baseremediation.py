######################### BASE CLASSES ###########################

from netmiko import ConnectHandler
import base64
import re


class BaseRemediation(object):

	def __init__(self,ip,hostname,username,password,vendor,type):
		self.ip = ip
   		self.hostname = hostname
   		self.username = username
   		self.password = password
   		self.vendor = vendor
   		self.type = type
		self.password_decrypt= base64.b64decode(self.password)

	def connect(self):
		if (self.type == 'switch'):
			self.net_connect = ConnectHandler(self.ip,self.hostname,self.username,self.password_decrypt,self.secret(),port=65500,device_type=self.device_call())
		else:
			self.net_connect = ConnectHandler(self.ip,self.hostname,self.username,self.password_decrypt,self.secret(),device_type=self.device_call())
			
	def secret(self):
		enable_secret = ''
		if (self.location() == 'wdstk'):
			enable_secret = base64.b64decode(self.password)
		elif (self.location() == 'ktch'):
			enable_secret = base64.b64decode(self.password)

		return enable_secret
		
	def location(self):
		datacenter_location = ''
		if (self.type == 'firewall'):
			location_list = self.hostname.split('-')	
			datacenter_location = location_list[3]

		elif (self.type == 'switch' or self.type == 'router'):
			location_list = self.hostname.split('.')	
			datacenter_location = location_list[3]

		return datacenter_location

	def device_call(self):
		device_attribute = ''
		if (self.type == 'router' or self.type == 'switch'):
			device_attribute = 'cisco_ios'
		
		elif (self.type == 'firewall'):
			device_attribute = 'cisco_asa'

		return device_attribute

	def get_error_message_interface(self,error_message):
		INTERFACE_RE = r'\s(.+?\d/\d/\d.)'
		interface = re.search(INTERFACE_RE,error_message).group(1)
		
		return interface
				
	def get_interface_status(self,interface):
		INTERFACE_STATUS_RE = r'\((.+?)\)'
		show_interface_status = self.net_connect.send_config('show interface status | include %s' % interface)
		list = show_interface_status.split('\n')[0]

		interface_status = re.search(INTERFACE_STATUS_RE,interface).group(1)

		return interface_status

