import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from backend.data_containers.Segment import Segment
from backend.data_containers.Process import Process

class Add_Segment_Dialog(Gtk.Dialog):
	def __init__(self,parent_window, parent_process):
		Gtk.Dialog.__init__(self, "Add Segment", parent_window)
		
		#create a grid layout
		grid = Gtk.Grid()

		#create the memory data container
		self.parent_process = parent_process

		#setting the spacings of the grid
		grid.set_column_homogeneous = True
		grid.set_column_spacing(20)
		grid.set_row_spacing(20)

		#setting up the 'Start Address' text field
		label_segment_name = Gtk.Label('Segment Name')
		self.segment_name_text = Gtk.Entry()


		#setting up the 'Size' text field
		label_segment_size_address = Gtk.Label('Segment Size')
		self.segment_size_text = Gtk.Entry()


		#setting up the 'Add Hole', 'Cancel' buttons
		self.add_segment_btn = Gtk.Button('Add Segment')
		self.add_segment_btn.connect('clicked', self.on_add_segment_clicked)
		self.cancel_btn = Gtk.Button('Cancel')
		self.cancel_btn.connect('clicked', self.on_cancel_clicked)

		#attaching the items to the grid
		grid.attach(label_segment_name, 	 0, 0, 1, 1)
		grid.attach(self.segment_name_text, 1, 0, 1, 1)

		grid.attach(label_segment_size_address, 0, 1, 1, 1)
		grid.attach(self.segment_size_text, 	1, 1, 1, 1)

		grid.attach(self.add_segment_btn, 0, 2, 1, 1)
		grid.attach(self.cancel_btn, 1, 2, 1, 1)
		
		#adding the grid layout we built to the dialog window
		self.get_content_area().add(grid)

		self.show_all()

	def on_add_segment_clicked(self, widget):
		segmetn_name = self.segment_name_text.get_text()
		segmetn_size = int(self.segment_size_text.get_text())

		#store the segment in process
		
		segment = Segment(self.parent_process, segmetn_name, segmetn_size)
		self.parent_process.add_segment(segment)
		self.destroy()

	def on_cancel_clicked(self, widget):
		self.destroy()