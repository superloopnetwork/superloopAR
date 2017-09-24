########################### LINK FAIL ############################

from initialize import Initialize

class Default(Initialize):

	def remediate(self,dstamp,tstamp,device,error_code,error_message):

		print 'DEFAULT REMEDIATION'

