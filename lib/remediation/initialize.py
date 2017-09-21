from baseremediation import BaseRemediation

########################## INIT. CLASS ###########################

class Initialize(BaseRemediation):

	def __init__(self,*arg):
		ip,hostname,username,password,vendor,type = arg
		BaseRemediation.__init__(self,ip,hostname,username,password,vendor,type)
