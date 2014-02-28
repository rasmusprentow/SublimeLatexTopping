import sublime, sublime_plugin, os

mainfilepath="../main.tex"
texcommand="%!TEX root"
texroot = texcommand + " = " + mainfilepath




class TexRootCommand(sublime_plugin.TextCommand):


	def run(obj, edit): 
		line = obj.view.substr(obj.view.line(0))
		if not line.startswith(texcommand):
			obj.view.insert(edit, 0, texroot + "\n")		


class Loader(sublime_plugin.EventListener):
	"""docstring for Loader"""

	def on_load(obj,view):  
		name = view.file_name()
		if "main.tex" not in name and "FrontBackmatter" not in name:
			fileName, fileExtension = os.path.splitext(name)
			if fileExtension == ".tex":
				view.run_command('tex_root')
 
	 
