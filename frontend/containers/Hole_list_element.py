import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from frontend.containers.list_element import list_element

class Hole_list_element(list_element):
	def __init__(self, label, hole_index, delete_callback_func):
		list_element.__init__(self, label)
		self.hole_index = hole_index
		self.delBtn.connect("clicked", delete_callback_func, hole_index)


		