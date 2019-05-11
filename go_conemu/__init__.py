from fman import DirectoryPaneCommand
import subprocess

class GoConemu(DirectoryPaneCommand):
	def __call__(self):
		conemu_path = "C:\\Program Files\\ConEmu\\ConEmu64.exe"
		current_path = rself.pane.get_path()[7:]
		subprocess.call(conemu_path + " -Dir " + current_path)