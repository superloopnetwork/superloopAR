########################### LINK FAIL ############################

from initialize import Initialize

class LinkFailure(Initialize):

	def troubleshoot(self):
		self.connect()
		print 'LINK FAILURE'

