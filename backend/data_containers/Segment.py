class Segment():
	def __init__(self, process_index, segment_index, name, size):
		self.process_index = process_index
		self.segment_index = segment_index
		self.name = name
		self.size = size
		self.start_address = -1

		