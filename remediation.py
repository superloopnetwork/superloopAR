######################## FUNCTIONS ##############################
from lib.remediation.link_failure import LinkFailure 
from mapping import get_remediation 

def remediation(dstamp,tstamp,device,error_code,error_message,ntw_device):

	module = get_remediation(error_code)

	device = module(*ntw_device)

	device.remediate(dstamp,tstamp,device,error_code,error_message)
