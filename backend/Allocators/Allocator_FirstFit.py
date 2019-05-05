from backend.Allocators.Allocator import Allocator

class Allocator_FirstFit():
	def __init__(self, memory, withCompaction):
		Allocator.__init__(self, memory, withCompaction)



	def allocate(self):
		#sort the holes by start address
		self.memory.holes = sorted(self.memory.holes, key=lambda k: 1/(k.start_address+1))

		for process in self.memory.processes:
			for segment in process.segments:
				allocated_success = False

				for hole in reversed(self.memory.holes):
					if self.memory.fill_hole(segment, hole) == 1: #try to allocate the segment
						allocated_success = True
						break #allocation was succesful

				if allocated_success == False:
					return 0 #failed to allocate
		return self.memory
					

		
