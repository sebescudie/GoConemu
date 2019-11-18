from fman import DirectoryPaneCommand, show_alert
import subprocess

class GoConemu(DirectoryPaneCommand):
	def __call__(self):
		conemu_path = "C:\\Program Files\\ConEmu\\ConEmu64.exe"
		current_path = self.pane.get_path()
		subprocess.call(f'"{conemu_path}" -Single -Dir "{as_human_readable(current_path)}"')