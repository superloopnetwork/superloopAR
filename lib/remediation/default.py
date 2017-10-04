########################### LINK FAIL ############################
from .. import globalvar
from initialize import Initialize

class Default(Initialize):

	def remediate(self,dstamp,tstamp,device,error_code,error_message):

		print dstamp, tstamp, device, error_code, error_message
		print '[EventID:%s]    [Device:%s]    Redemdiation: Default' % (globalvar.event_id,device)
		globalvar.event_id = globalvar.event_id + 1
		print
