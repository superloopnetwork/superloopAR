########################### LINK FAIL ############################
from .. import globalvar
import re


from initialize import Initialize

class LinkFailure(Initialize):

	def remediate(self,dstamp,tstamp,device,error_code,error_message):
#		interface = self.get_error_message_interface(error_message)
#
#		self.connect()
#		interface_status = self.net_connect.send_command_expect('show interface %s | %s' % interface)
#
#		if('connected' in output):
#			print 'REMEDIATION: TRUE'
#		else:
#			print 'R' 

		print dstamp, tstamp, device, error_code, error_message
		print '[EventID:%s]    [Device:%s]    Redemdiation: LinkFailure' % (globalvar.event_id,device)
		globalvar.event_id = globalvar.event_id + 1
		print
