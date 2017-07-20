import asyncio, asyncpg
from .Class import Class

class Player:
	
	__slots__ = (
		'member', 'pool', 'level',
		'str_', 'dex', 'int_', 'wis', 'luk', 'cha',
	)

	EXTERNAL = ('member', 'pool', 'level')
	
	# RW = 20
	# F = 5
	# ST = 7

	# def __init__(self, member, str_, dex, int_, luk, cha):
		# self.pool = person.pool
		# self.member = person
		
		# stats = ['str', 'dex', 'int_', 'luk', 'cha', 
		# self.rw = self.RW
		# self.str_ = str_
		# self.dex = dex
		# self.int_ = int_
		# self.luk = luk
		# self.cha = cha
		# self.att = self.str_ # + self.level
		# self.weapon = None
		# self.shield = None
		# self.fl = math.floor(self.F + (1.2 * dex))
		# self.st = math.floor(self.ST + (1.2 * int_))
		
	@classmethod
	async def load(cls, member):
		self = Player()
		
		self.member = member
		self.pool = member.pool
		self.level = member.localLevel
		
		for slot in self.__slots__:
			if slot not in self.EXTERNAL:
				data = await self.member.getRPGStats(slot)
				
				setattr(self, slot, data[0])
			
		return self
		
	@property
	def att(self):
		pass
	
	def equip(self, item):
		{
			'weapon': setattr(self, 'weapon', item),
			'shield': setattr(self, 'shield', item),
		}.get(item.type)
		
		self.att += item.att
		self.st += item.st
		self.str_ += item.str_	
		self.dex += item.dex	
		self.int_ += item.int_
		self.cha += item.cha
		
	def take_damage(self, damage):
		self.rw = self.rw - damage