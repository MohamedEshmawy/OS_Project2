class Segment():
	def __init__(self, process_id, name, size, segment_id = 0):
		self.process_id = process_id
		self.segment_id = segment_id
		self.name = name
		self.size = size
		self.start_address = -1

	def set_id(segment_id):
		self.segment_id = segment_id
		