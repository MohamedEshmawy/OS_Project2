class Segment():
	def __init__(self, parent_process, name, size, segment_id = 0):
		self.parent_process = parent_process
		self.segment_id = segment_id
		self.name = name
		self.size = size
		self.start_address = -1

	def set_id(self, segment_id):
		self.segment_id = segment_id
		