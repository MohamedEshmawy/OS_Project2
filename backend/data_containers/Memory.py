from backend.data_containers.Process import Process

class Memory():
	def __init__(self):
		self.size = 0
		self.holes = []
		self.processes = []

	def __del__(self):
		for process in self.processes:
			del process
		for hole in self.holes:
			del hole

	def add_process(self, process):
		self.processes.append(process)

	def remove_process(self, process_index):
		self.processes.pop(process_index)

	def add_hole(self, hole):
		self.holes.append(hole)

	def remove_hole(self, hole_index):
		self.holes.pop(hole_index)

	def set_size(self, size):
		self.size = size
		