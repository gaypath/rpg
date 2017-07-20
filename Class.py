import json
import random

def load_class(id):
	with open('classes/{}.json'.format(str(id)), 'r') as f:
		clss = json.loads(f.read())
	
	return clss

class Class:
	def __init__(self, id, level):
		self.load = load_class(id)
		self.level = level
		self.name = self.load['name']
		
	@property
	def hit_die(self):
		if self.level == 1:
			return self.load['hit_die'][0] * self.load['hit_die'][1]
		else:
			hd = 0
			for i in range(self.load['hit_die'][0]):
				hd += random.randint(1, self.load['hit_die'][1])
				
			return hd
	
			