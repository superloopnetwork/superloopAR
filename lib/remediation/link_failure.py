########################### LINK FAIL ############################

from initialize import Initialize

class LinkFailure(Initialize):

	def remediate(self,dstamp,tstamp,device,error_code,error_message):
		print 'LINK FAILURE'
		print dstamp,device

