from backend.data_containers.Process import Process
from backend.data_containers.Hole import Hole

class Memory():
	def __init__(self):
		self.size = 0
		self.holes = []
		self.allocated_holes = []
		self.processes = []

		self.hole_id = 0
		self.allocated_hole_id = 0
		self.process_id = 0

	def __del__(self):
		for process in self.processes:
			del process
		for hole in self.holes:
			del hole

	def add_process(self, process):
		process.set_id(self.process_id)
		self.processes.append(process)
		self.process_id += 1

	def remove_process(self, process_id):
		counter = 0
		for process in self.processes:
			if process.process_id == process_id:
				self.processes.pop(counter)
			counter += 1
		

	def add_hole(self, hole):
		hole.set_id(self.hole_id)
		self.holes.append(hole)
		self.hole_id += 1

	def remove_hole(self, hole_id):
		counter = 0
		for hole in self.holes:
			if hole.hole_id == hole_id:
				self.holes.pop(counter)
			counter += 1

	def add_allocated_hole(self, allocated_hole):
		allocated_hole.set_id(self.allocated_hole_id)
		self.allocated_holes.append(allocated_hole)
		self.allocated_hole_id += 1

	def remove_allocated_hole(self, allocated_hole_id):
		counter = 0
		for allocated_hole in self.allocated_holes:
			if allocated_hole.allocated_hole_id == allocated_hole_id:
				self.allocated_holes.pop(counter)
			counter += 1





	def set_size(self, size):
		self.size = size
		for i in range(0,len(self.allocated_holes)):
			self.allocated_holes.pop(0)
		address_counter = 0
		self.holes = sorted(self.holes, key=lambda k: k.start_address)
		for hole in self.holes:
			if hole.start_address > address_counter:
				self.add_allocated_hole(Hole(address_counter, hole.start_address-address_counter))
			address_counter = hole.start_address + hole.size
		last_hole = self.holes[len(self.holes)-1]
		if last_hole.start_address + last_hole.size < self.size:
			self.add_allocated_hole(Hole(last_hole.start_address + last_hole.size, self.size-(last_hole.start_address + last_hole.size)))

		
	def fill_hole(self, segment, hole):
		if segment.size > hole.size:
			return 0
		segment.start_address = hole.start_address
		hole.start_address += segment.size
		hole.size -= segment.size
		if hole.size == 0:
			self.remove_hole(hole.hole_id)
		return 1