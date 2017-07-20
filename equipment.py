def load_equip(id):
	with open("rpg/equipment/{}.json".format(str(id)), "r") as f:
		weapon = json.loads(f.read())
		
	return weapon

class Equipment:
	def __init__(self, **kwargs):
		self.type = kwargs.get('type')
		self.weight = kwargs.get('weight', 1)
		self.att = kwargs.get('pp', 0)
		self.st = kwargs.get('st', 0)
		self.str_ = kwargs.get('str', 0)
		self.dex = kwargs.get('dex', 0)
		self.int_ = kwargs.get('int_', 0)
		self.luk = kwargs.get('luk', 0)
		self.cha = kwargs.get('cha', 0)