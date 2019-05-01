import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from frontend.containers.list_element import list_element

class Process_list_element(list_element):
	def __init__(self, label, process, delete_callback_func):
		list_element.__init__(self, label, delBtnLabel = "Edit")
		self.process = process
		self.delBtn.connect("clicked", delete_callback_func, process)


		