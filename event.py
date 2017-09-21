######################## FUNCTIONS ##############################
from lib.objects.event import Event
from remediation import remediation

def event(dstamp,tstamp,device,error_code,error_message,ntw_device):

	e = Event(dstamp,tstamp,device,error_code,error_message)

	remediation(e.datestamp,e.timestamp,e.device,e.error_code,e.error_message,ntw_device)
