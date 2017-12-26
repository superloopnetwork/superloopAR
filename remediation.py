######################## FUNCTIONS ##############################
from lib.remediation.link_failure import LinkFailure 
from mapping import get_remediation 

def remediation(dstamp,tstamp,ip_address,error_code,error_message,ntw_device):

	# MODULE VARIABLE CALLS THE GET_REMEDIATION FUNCTION AND RETURNS THE SPECIFIC REMEDIATION REQUIRED TO BE USED WITHIN THE LIB/REMEDIATION DIRECTORY
	module = get_remediation(error_code)

	# DEVICE CREATES AN OBJECT OF THE DEVICE USING NTW_DEVICE(LIST) FROM THE ABOVE MODULE VARIABLE(CLASS)
	device = module(*ntw_device)

	# CALLING THE REMEDIATE METHOD WITHIN THE SPECIFIED CLASS
	device.remediate(dstamp,tstamp,ip_address,error_code,error_message)
