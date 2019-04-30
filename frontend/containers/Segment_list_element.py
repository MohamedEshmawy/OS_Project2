import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from frontend.containers.list_element import list_element

class Segment_list_element(list_element):
	def __init__(self, label, process_index, segment_index, delete_callback_func):
		list_element.__init__(self, label)
		self.segment_index = segment_index
		self.process_index = process_index
		self.delBtn.connect("clicked", delete_callback_func, process_index, segment_index)


		