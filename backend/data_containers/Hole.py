class Hole():
	def __init__(self, start_address, size, hole_id = 0):
		self.start_address = start_address
		self.size = size
		self.hole_id = hole_id
	
	def set_id(self, hole_id):
		self.hole_id = hole_id

