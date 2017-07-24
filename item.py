import json

def load_item(id):
	with open("rpg/items/{}.json".format(str(id)), "r") as f:
		item = json.loads(f.read())
	
	switch = {
		"1": Equipment(item)
	}.get(str(item['item_type']), None)
	
	return switch

class Equipment:
	def __init__(self, equipment):
		
		self.id = equipment.get('id', 0)
		self.inventoryitem_id = equipment.get('inventoryitem_id', 0)
		self.item_type = 1
		self.name = equipment.get('name')
		self.type = equipment.get('type')
		self.weight = equipment.get('weight', 1)
		self.att = equipment.get('att', 0)
		self.def_ = equipment.get('def', 0)
		self.str_ = equipment.get('str_', 0)
		self.dex = equipment.get('dex', 0)
		self.int_ = equipment.get('int_', 0)
		self.luk = equipment.get('luk', 0)
		self.cha = equipment.get('cha', 0)
		self.upgrade_slots = equipment.get('upgrade_slots', 0)
	
	@property
	def equip_stats(self):
		return {
			'att': self.att,
			'def_': self.def_,
			'str_': self.str_,
			'dex': self.dex,
			'int_': self.int_,
			'luk': self.luk,
			'cha': self.cha,
		}
		
	@property
	def equip_type(self):
		return {
			"1": "1h Weapon",
			"2": "2h Weapon",
			"3": "Ranged",
			"4": "Shield",
			"5": "Hat",
		}.get(str(self.type), 'None')