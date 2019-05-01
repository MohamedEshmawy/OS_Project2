import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from frontend.Views.Config_Memory_Dialog import Config_Memory_Dialog


class Main_Window_Grid(Gtk.Grid):
	def __init__(self, parent_view):
		Gtk.Grid.__init__(self)
		self.parent_view = parent_view

		#create the memory data container
		self.memory = Memory()

		#setting the spacings of the grid
		self.set_column_homogeneous = True
		self.set_column_spacing(20)
		self.set_row_spacing(20)

		#setting up the allocator algorithm radio buttons
		self.radio_firstFit = Gtk.RadioButton.new_with_label_from_widget(None, "First Fit")
		self.radio_bestFit  = Gtk.RadioButton.new_with_label_from_widget(self.radio_firstFit, "Best Fit")
		self.radio_worstFit = Gtk.RadioButton.new_with_label_from_widget(self.radio_firstFit, "Worst Fit")

		#setting up the uneditable 'size' text field
		self.size_text = Gtk.Entry()
		self.size_text.set_editable(False)
		box_size = Gtk.Box(spacing=6)
		box_size.pack_start(Gtk.Label('Size'), True, True, 0)
		box_size.pack_start(self.size_text, True, True, 0)

		#setting up the 'Config Memory', 'Add Process', 'Start' buttons
		config_memory_btn = Gtk.Button('Config Memory')
		config_memory_btn.connect('clicked', self.config_memory_dialog)
		add_process_btn = Gtk.Button('Add Process')
		start_btn = Gtk.Button('Start')


		#setting up "With Compaction" check box
		self.with_compaction_chk = Gtk.CheckButton()
		box_compaction = Gtk.Box(spacing=6)
		box_compaction.pack_start(Gtk.Label('With Compaction'), True, True, 0)
		box_compaction.pack_start(self.with_compaction_chk, True, True, 0)

		#setting up the list box to hold segments
		self.listbox = Gtk.ListBox()

		#attaching
		self.attach(self.radio_firstFit, 0, 0, 1, 1)
		self.attach(self.radio_bestFit, 0, 1, 1, 1)
		self.attach(self.radio_worstFit, 0, 2, 1, 1)

		self.attach(box_size, 0, 3, 1, 1)

		self.attach(config_memory_btn, 0, 4, 1, 1)
		self.attach(add_process_btn, 0, 5, 1, 1)
		self.attach(start_btn, 0, 6, 1, 1)

		self.attach(box_compaction, 0, 7, 1, 1)

		self.attach(self.listbox, 4, 0, 15, 8)

	def config_memory_dialog(self, widget):
		dialog = Config_Memory_Dialog(self.parent_view, self.memory)
		dialog.show_all()
