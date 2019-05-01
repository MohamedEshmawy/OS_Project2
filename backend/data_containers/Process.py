from backend.data_containers.Segment import Segment

class Process():
	def __init__(self, process_index, name):
		self.process_index = process_index
		self.name = name
		self.segments = []

	def __del__(self):
		for segment in self.segments:
			del segment

	def add_segment(self, segment):
		self.segments.append(segment)

	def remove_segment(self, segment_index):
		self.segments.pop(segment_index)

		