from fman import DirectoryPaneCommand
from subprocess import run

class GoConemu(DirectoryPaneCommand):
	def __call__(self):
		conemu_path = "C:\\Program Files\\ConEmu\\ConEmu64.exe"
		current_path = self.pane.get_path()[7:]
		run(conemu_path + " -Dir " + current_path)