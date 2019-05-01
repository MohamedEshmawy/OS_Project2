from backend.data_containers.Process import Process

class Memory():
	def __init__(self):
		self.size = 0
		self.holes = []
		self.processes = []

		self.hole_id = 0
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
		self.processes.pop(process_id)

	def add_hole(self, hole):
		hole.set_id(self.hole_id)
		self.holes.append(hole)
		self.hole_id += 1

	def remove_hole(self, hole_id):
		self.holes.pop(hole_id)

	def set_size(self, size):
		self.size = size
		