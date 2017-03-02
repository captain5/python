import sys
from cliff.app import App
from cliff.commandmanager import CommandManager


class XQShell(App):

    def __init__(self):
        self.token = None
        self.baseurl = None
        self.NAME = 'xqshell'
        super(XQShell, self).__init__(
            description='xiaoqiang command shell',
            version='0.1',
            command_manager=CommandManager('cliff.xqshell'),
            deferred_help=True)

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = XQShell()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[:-1]))
