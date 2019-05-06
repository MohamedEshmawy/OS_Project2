from backend.data_containers.Memory import Memory
import copy

class Allocator():
	def __init__(self, memory, withCompaction):
		self.memory = copy.deepcopy(memory)
		if withCompaction == True:
			self.memory.compact()


	def allocate():
		pass
		
