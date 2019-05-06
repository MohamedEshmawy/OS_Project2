import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from frontend.Views.Add_Hole_Dialog import Add_Hole_Dialog
from frontend.containers.Hole_list_element import Hole_list_element

class Config_Memory_Dialog(Gtk.Dialog):
	def __init__(self,parent_view, memory):
		Gtk.Dialog.__init__(self, "Config Memory", parent_view)

		#storing the parent_view
		self.parent_view = parent_view

		#create a grid layout
		grid = Gtk.Grid()

		#create the memory data container
		self.memory = memory

		#setting the spacings of the grid
		grid.set_column_homogeneous = True
		grid.set_column_spacing(20)
		grid.set_row_spacing(20)

		#setting up the uneditable 'size' text field
		self.size_text = Gtk.Entry()
		box_size = Gtk.Box(spacing=6)
		box_size.pack_start(Gtk.Label('Size'), True, True, 0)
		box_size.pack_start(self.size_text, True, True, 0)

		#setting up the 'Add Hole', 'Done' buttons
		self.add_hole_btn = Gtk.Button('Add Hole')
		self.add_hole_btn.connect('clicked', self.on_add_hole_clicked)
		self.done_btn = Gtk.Button('Done')
		self.done_btn.connect('clicked', self.on_done_clicked)

		#setting up the list box to hold holes
		self.hole_listbox = Gtk.ListBox()
		self.hole_listbox.set_border_width(4)




		#attaching the items to the grid
		grid.attach(box_size, 0, 3, 1, 1)

		grid.attach(self.add_hole_btn, 0, 5, 1, 1)
		grid.attach(self.done_btn, 0, 6, 1, 1)

		grid.attach(self.hole_listbox, 4, 0, 15, 8)

		#if memory already had holes then show them
		self.update_hole_list_box()
		#adding the grid layout we built to the dialog window
		self.get_content_area().add(grid)

		self.show_all()


	def on_done_clicked(self, widget):
		self.memory.set_size(int(self.size_text.get_text()))
		self.destroy()

	def on_add_hole_clicked(self, widget):
		dialog = Add_Hole_Dialog(self.parent_view, self.memory)
		response = dialog.run()
		self.update_hole_list_box()

		
	def update_hole_list_box(self):
		#clear the list
		for child in self.hole_listbox.get_children():
			self.hole_listbox.remove(child)

		for hole in self.memory.holes:
			label = "Hole"+ str(hole.hole_id) +", Start Address: "+ str(hole.start_address) +", Size: "+ str(hole.size)
			hole_list_element = Hole_list_element(label, hole.hole_id, self.hole_delete_callback_func)
			self.hole_listbox.add(hole_list_element)
		self.hole_listbox.show_all()
		self.size_text.set_text(str(self.memory.size))

	def hole_delete_callback_func(self, widget, *data):
		hole_id = data[0]
		self.memory.remove_hole(hole_id)
		self.update_hole_list_box()