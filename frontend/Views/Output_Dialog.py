import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from frontend.extra.Colored_Label import Colored_Label
import random

class Output_Dialog(Gtk.Dialog):
	def __init__(self,parent_view, memory):
		Gtk.Dialog.__init__(self, "Output", parent_view)

		#set the dialog width
		width = 1000

		#storing the parent_view
		self.parent_view = parent_view

		#create a grid layout
		grid = Gtk.Grid()

		#create the memory data container
		self.memory = memory

		#calculate the column spacing
		column_spacing = width / memory.size
		if column_spacing < 1:
			column_spacing = 1

		#setting the spacings of the grid
		grid.set_column_homogeneous = True
		grid.set_column_spacing(column_spacing)
		grid.set_row_spacing(20)

		for process in memory.processes:
			for segment in process.segments:
				#generate the label
				label = "P:"+ str(process.name) +"	S: "+ str(segment.name)
				#generate the color
				color = "#%02xf0" % random.randint(0, 0xFF) + "%02x" % random.randint(0, 0xFF)
				#create the color label
				color_label = Colored_Label(label, color)
				#create the start address label
				start_address_label = Gtk.Label(str(segment.start_address))
				#attach the colorlabel
				grid.attach(color_label, segment.start_address, 0, segment.size, 10)
				#attach the start address label
				grid.attach(start_address_label, segment.start_address, 10, 1, 1)

		for hole in memory.holes:
			#generate the label
			label = "Hole:"+ str(hole.hole_id)
			#generate the color
			color = "#7F7F7F"				
			#create the color label
			color_label = Colored_Label(label, color)
			#create the start address label
			start_address_label = Gtk.Label(str(hole.start_address))
			#attach the colorlabel
			grid.attach(color_label, hole.start_address, 0, hole.size, 10)
			#attach the start address label
			grid.attach(start_address_label, hole.start_address, 10, 1, 1)

		for allocated_hole in memory.allocated_holes:
			#generate the label
			label = "Allocated Space:"+ str(allocated_hole.hole_id)
			#generate the color
			color = "#000000"				
			#create the color label
			color_label = Colored_Label(label, color)
			#create the start address label
			start_address_label = Gtk.Label(str(allocated_hole.start_address))
			#attach the colorlabel
			grid.attach(color_label, allocated_hole.start_address, 0, allocated_hole.size, 10)
			#attach the start address label
			grid.attach(start_address_label, allocated_hole.start_address, 10, 1, 1)

		#insert the final address at the end of the memory
		end_address_label = Gtk.Label(str(memory.size))
		grid.attach(end_address_label, memory.size, 10, 1, 1)
			
			
			
			



		#adding the grid layout we built to the dialog window
		self.get_content_area().add(grid)

		self.show_all()