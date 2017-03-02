#login.py
import logging
from cliff.command import Command
class Login(Command):
	"My first cliff!"
	log = logging.getLogger(__name__)
	def take_action(self, parsed_args):
		self.log.info('sending greeting')
		self.log.debug('debugging')
		self.app.stdout.write('hi!\n')
		print 'success'
		print 'error'