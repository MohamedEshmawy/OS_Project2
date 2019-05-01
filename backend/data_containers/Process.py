from backend.data_containers.Segment import Segment

class Process():
	def __init__(self, name = '', process_id = 0):
		self.process_id = process_id
		self.name = name
		self.segments = []

		self.segment_id = 0

	def __del__(self):
		for segment in self.segments:
			del segment

	def add_segment(self, segment):
		segment.set_id(self.segment_id)
		self.segments.append(segment)
		self.segment_id += 1


	def remove_segment(self, segment_id):
		counter = 0
		for seg in self.segments:
			if seg.segment_id == segment_id:
				self.segments.pop(counter)
			counter += 1
		

	def set_id(self, process_id):
		self.process_id = process_id

	def set_name(self, name):
		self.name = name