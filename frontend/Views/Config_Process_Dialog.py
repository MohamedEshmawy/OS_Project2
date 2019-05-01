import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from backend.data_containers.Process import Process
from frontend.Views.Add_Segment_Dialog import Add_Segment_Dialog
from frontend.containers.Segment_list_element import Segment_list_element

class Config_Process_Dialog(Gtk.Dialog):
	def __init__(self,parent_view, memory, process):
		Gtk.Dialog.__init__(self, "Config Process", parent_view)

		#storing the parent_view
		self.parent_view = parent_view

		#storing the process
		self.process = process

		#store the memory
		self.memory = memory

		#create a grid layout
		grid = Gtk.Grid()

		#setting the spacings of the grid
		grid.set_column_homogeneous = True
		grid.set_column_spacing(20)
		grid.set_row_spacing(20)

		#setting up the 'Process Name' text field
		self.process_name_text = Gtk.Entry()
		self.process_name_text.set_text(self.process.name)
		box_process_name = Gtk.Box(spacing=6)
		box_process_name.pack_start(Gtk.Label('Process Name'), True, True, 0)
		box_process_name.pack_start(self.process_name_text, True, True, 0)

		#setting up the 'Add Segment', 'Done' , 'Delete' buttons
		self.add_segment_btn = Gtk.Button('Add Segment')
		self.add_segment_btn.connect('clicked', self.on_add_segment_clicked)
		self.done_btn = Gtk.Button('Done')
		self.done_btn.connect('clicked', self.on_done_clicked)
		self.delete_btn = Gtk.Button('Delete')
		self.delete_btn.connect('clicked', self.on_delete_clicked)

		#setting up the list box to hold segments
		self.segment_listbox = Gtk.ListBox()
		self.segment_listbox.set_border_width(4)

		#attaching the items to the grid
		grid.attach(box_process_name, 0, 3, 1, 1)

		grid.attach(self.add_segment_btn, 0, 5, 1, 1)
		grid.attach(self.done_btn, 0, 6, 1, 1)

		grid.attach(self.segment_listbox, 4, 0, 15, 8)

		#if memory already had holes then show them
		self.update_segment_list_box()

		#adding the grid layout we built to the dialog window
		self.get_content_area().add(grid)

		self.show_all()

	def on_done_clicked(self, widget):
		self.process.set_name(self.process_name_text.get_text())
		self.destroy()

	def on_add_segment_clicked(self, widget):
		dialog = Add_Segment_Dialog(self.parent_view, self.process)
		response = dialog.run()
		self.update_segment_list_box()

	def on_delete_clicked(self, widget):
		self.memory.remove_process(self.process.process_id)
		self.destroy()
		
	def update_segment_list_box(self):
		#clear the list
		for child in self.segment_listbox.get_children():
			self.segment_listbox.remove(child)

		for segment in self.process.segments:
			label = "segment:"+ str(segment.name) +", Size: "+ str(segment.size)
			segment_list_element = Segment_list_element(label, self.process, segment.segment_id, self.segment_delete_callback_func)
			self.segment_listbox.add(segment_list_element)
		self.segment_listbox.show_all()

	def segment_delete_callback_func(self, widget, *data):
		parent_process = data[0]
		segment_id = data[1]
		parent_process.remove_segment(segment_id)
		self.update_segment_list_box()