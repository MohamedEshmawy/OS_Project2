import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from backend.data_containers.Hole import Hole

class Add_Hole_Dialog(Gtk.Dialog):
	def __init__(self,parent_window, memory):
		Gtk.Dialog.__init__(self, "Add Hole", parent_window)
		
		#create a grid layout
		grid = Gtk.Grid()

		#create the memory data container
		self.memory = memory

		#setting the spacings of the grid
		grid.set_column_homogeneous = True
		grid.set_column_spacing(20)
		grid.set_row_spacing(20)

		#setting up the 'Start Address' text field
		label_start_address = Gtk.Label('Start Address')
		self.start_address_text = Gtk.Entry()


		#setting up the 'Size' text field
		label_size_address = Gtk.Label('Size')
		self.size_text = Gtk.Entry()


		#setting up the 'Add Hole', 'Cancel' buttons
		self.add_hole_btn = Gtk.Button('Add Hole')
		self.add_hole_btn.connect('clicked', self.on_add_hole_clicked)
		self.cancel_btn = Gtk.Button('Cancel')
		self.cancel_btn.connect('clicked', self.on_cancel_clicked)

		#attaching the items to the grid
		grid.attach(label_start_address, 	 0, 0, 1, 1)
		grid.attach(self.start_address_text, 1, 0, 1, 1)

		grid.attach(label_size_address, 0, 1, 1, 1)
		grid.attach(self.size_text, 	1, 1, 1, 1)

		grid.attach(self.add_hole_btn, 0, 2, 1, 1)
		grid.attach(self.cancel_btn, 1, 2, 1, 1)

		#adding the grid layout we built to the dialog window
		self.get_content_area().add(grid)

		self.show_all()

	def on_add_hole_clicked(self, widget):
		start_address = int(self.start_address_text.get_text())
		size = int(self.size_text.get_text())

		#store the hole data in memory
		hole = Hole(start_address, size)
		self.memory.add_hole(hole)
		self.destroy()


	def on_cancel_clicked(self, widget):
		self.destroy()