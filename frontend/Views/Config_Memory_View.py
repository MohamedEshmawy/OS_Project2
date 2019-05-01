import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory

class Config_Memory_View(Gtk.Dialog):
	def __init__(self,view, memory):
		Gtk.Dialog.__init__('Config Memory', view)
		grid = Gtk.Grid(self)
		#create the memory data container
		self.memory = Memory

		#setting the spacings of the grid
		grid.set_column_homogeneous = True
		grid.set_column_spacing(20)
		grid.set_row_spacing(20)

		#setting up the uneditable 'size' text field
		grid.size_text = Gtk.Entry()
		box_size = Gtk.Box(spacing=6)
		box_size.pack_start(Gtk.Label('Size'), True, True, 0)
		box_size.pack_start(grid.size_text, True, True, 0)

		#setting up the 'Add Hole', 'Done' buttons
		grid.add_hole_btn = Gtk.Button('Add Hole')
		grid.done_btn = Gtk.Button('Done')


		#setting up the list box to hold segments
		grid.listbox = Gtk.ListBox()

		#attaching

		grid.attach(box_size, 0, 3, 1, 1)

		grid.attach(grid.add_hole_btn, 0, 5, 1, 1)
		grid.attach(grid.done_btn, 0, 6, 1, 1)

		grid.attach(grid.listbox, 4, 0, 15, 8)