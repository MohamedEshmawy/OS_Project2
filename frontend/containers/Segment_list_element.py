import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from frontend.containers.list_element import list_element

class Segment_list_element(list_element):
	def __init__(self, label, parent_process, segment_id, delete_callback_func):
		list_element.__init__(self, label)
		self.segment_id = segment_id
		self.parent_process = parent_process
		self.delBtn.connect("clicked", delete_callback_func, self.parent_process, self.segment_id)


		