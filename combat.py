import random

class Combat:
	
	def __init__(self, attacker, defender):
		self.attacker = attacker
		self.defender = defender
		# self.order = [self.defender, self.attacker]
		self.turn = 1
		self.victor = False
	
	def tick(self):
		# new_order = []
		# for i in range(0, len(self.order)-1)
			# if i == len(self.order)-1:
				# new_order.append(self.order[0])
			# else:
				# new_order.append(self.order[i+1])
		
		# self.order = new_order
		self.turn += 1
	
	def swing(self):
		if self.turn % 2 != 0:
			str_ = self.defender.str_ * .85
			
			if (random.randint(1,20) + str_) > self.attacker.st:
				if self.defender.weapon:
					self.attacker.rw = self.attacker.rw - (self.defender.weapon.att + str_)
				else:
					self.attacker.rw = self.attacker.rw - str_
			
		else:
			st = self.defender.st * 1.15
			
			if (random.randint(1,20) + self.attacker.str_) > st:
				if self.attacker.weapon:
					self.defender.rw = self.defender.rw - (self.attacker.weapon.att + self.attacker.str_)
				else:
					self.defender.rw = self.attacker.rw - random.randint(1,self.attacker.str_)
		
		if self.defender.rw <= 0:
			self.victor = 1
		elif self.attacker.rw <= 0:
			self.victor = 2
			
	def raid(self):
		'''
		If (str + level) + roll is higher than defending (dex + (def +(.5*level))) + roll
		'''
		attack_roll = (self.attacker.str_ + self.attacker.level) + random.randint(1,20)
		defense_roll = (self.defender.dex + (self.defender.rw + (.5 * self.defender.level))) + random.randint(1,20)
		
		if attack_roll > defense_roll:
			pass