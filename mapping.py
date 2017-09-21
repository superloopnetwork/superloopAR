######################## FUNCTIONS ##############################
from lib.remediation import link_failure 
from lib.remediation import default 

ERROR_CODES_TO_REMEDIATIONS = {
	'LINEPROTO-5-UPDOWN': link_failure.LinkFailure
}

DEFAULT_REMEDIATION = {
	'default': default.Default
}

def get_remediation(error_code):

	if error_code in ERROR_CODES_TO_REMEDIATIONS:
		module = ERROR_CODES_TO_REMEDIATIONS[error_code]
	else:
		module = DEFAULT_REMEDIATION['default']

	return module
