########################## BASE CLASS ############################

class Event(object):
	def __init__(self,datestamp,timestamp,device,error_code,error_message):
		self.datestamp = datestamp
		self.timestamp = timestamp
		self.device = device
		self.error_code = error_code
		self.error_message = error_message 
