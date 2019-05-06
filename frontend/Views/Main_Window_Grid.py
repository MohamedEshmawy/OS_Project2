import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from backend.Allocators.Allocator_WorstFit import Allocator_WorstFit
from backend.Allocators.Allocator_BestFit import Allocator_BestFit
from backend.Allocators.Allocator_FirstFit import Allocator_FirstFit

from frontend.Views.Config_Memory_Dialog import Config_Memory_Dialog
from frontend.Views.Add_Process_Dialog import Add_Process_Dialog
from frontend.Views.Config_Process_Dialog import Config_Process_Dialog
from frontend.containers.Process_list_element import Process_list_element
from frontend.Views.Output_Dialog import Output_Dialog
from frontend.Views.Error_Dialog import Error_Dialog

#''' for test
from backend.data_containers.Hole import Hole
from backend.data_containers.Process import Process
from backend.data_containers.Segment import Segment
#'''

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

		#setting up the labe 'size'
		self.size_text = Gtk.Label('')
		box_size = Gtk.Box(spacing=6)
		box_size.pack_start(Gtk.Label('Size'), True, True, 0)
		box_size.pack_start(self.size_text, True, True, 0)

		#setting up the 'Config Memory', 'Add Process', 'Start' buttons
		config_memory_btn = Gtk.Button('Config Memory')
		config_memory_btn.connect('clicked', self.config_memory_dialog)
		add_process_btn = Gtk.Button('Add Process')
		add_process_btn.connect('clicked', self.add_process_dialog)
		start_btn = Gtk.Button('Start')
		start_btn.connect('clicked', self.output_dialog)

		#setting up "With Compaction" check box
		self.with_compaction_chk = Gtk.CheckButton()
		box_compaction = Gtk.Box(spacing=6)
		box_compaction.pack_start(Gtk.Label('With Compaction'), True, True, 0)
		box_compaction.pack_start(self.with_compaction_chk, True, True, 0)

		#setting up the list box to hold segments
		self.process_listbox = Gtk.ListBox()

		self.box_output = Gtk.Box()
		

		#attaching
		self.attach(self.radio_firstFit, 0, 0, 1, 1)
		self.attach(self.radio_bestFit, 0, 1, 1, 1)
		self.attach(self.radio_worstFit, 0, 2, 1, 1)

		self.attach(box_size, 0, 3, 1, 1)

		self.attach(config_memory_btn, 0, 4, 1, 1)
		self.attach(add_process_btn, 0, 5, 1, 1)
		self.attach(start_btn, 0, 6, 1, 1)

		self.attach(box_compaction, 0, 7, 1, 1)

		self.attach(self.process_listbox, 4, 0, 15, 8)

		self.attach(self.box_output, 0, 8, 50, 2)

		#for testing
		#'''
		P0 = Process(name = "P0")
		P1 = Process(name = "P1")

		P0S0 = Segment(P0, "S0", 50)
		P0S1 = Segment(P0, "S1", 25)
		P1S0 = Segment(P1, "S0", 50)

		H0 = Hole(0, 65)
		H1 = Hole(100, 35)

		P0.add_segment(P0S0)
		P0.add_segment(P0S1)
		P1.add_segment(P1S0)

		self.memory.add_process(P0)
		self.memory.add_process(P1)
		self.memory.add_hole(H0)
		self.memory.add_hole(H1)

		self.memory.set_size(200)

		self.update_process_list_box()
		#'''

	def config_memory_dialog(self, widget):
		dialog = Config_Memory_Dialog(self.parent_view, self.memory)
		dialog.run()
		self.update_process_list_box()

	def add_process_dialog(self, widget):
		dialog = Add_Process_Dialog(self.parent_view, self.memory)
		dialog.run()
		self.update_process_list_box()

	def output_dialog(self, widget):
		if self.radio_firstFit.get_active():
			allocator = Allocator_FirstFit(self.memory, self.with_compaction_chk.get_active())
			allocated_memory = allocator.allocate()

		if self.radio_bestFit.get_active():
			allocator = Allocator_BestFit(self.memory, self.with_compaction_chk.get_active())
			allocated_memory = allocator.allocate()

		if self.radio_worstFit.get_active():
			allocator = Allocator_WorstFit(self.memory, self.with_compaction_chk.get_active())
			allocated_memory = allocator.allocate()

		try:
			#clear the box
			for child in self.box_output.get_children():
				self.box_output.remove(child)
			self.box_output.pack_start(Output_Dialog(allocated_memory), True, True, 0)
			self.box_output.show_all()
		except Exception as e:
			if(allocated_memory == 0):
				dialog = Error_Dialog(self.parent_view, 'Failed to allocate')
				dialog.run()




	def update_process_list_box(self):
		self.size_text.set_text(str(self.memory.size))
		#clear the list
		for child in self.process_listbox.get_children():
			self.process_listbox.remove(child)

		for process in reversed(self.memory.processes):
			if len(process.segments) == 0:
				self.memory.remove_process(process.process_id)
				continue
			label = "process:"+ str(process.name) +", number of segments: "+ str(len(process.segments))
			process_list_element = Process_list_element(label, process, self.process_edit_callback_func)
			self.process_listbox.add(process_list_element)
		self.process_listbox.show_all()

	def process_edit_callback_func(self, widget, *data):
		process = data[0]
		dialog = Config_Process_Dialog(self.parent_view, self.memory, process)
		dialog.run()
		self.update_process_list_box()