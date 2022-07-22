import os
import random

class Hero():
	def __init__(self,role, dd, hp, ex, max_hp):
		self.role = role
		self.dd = dd
		self.hp = hp
		self.max_hp = max_hp

	def upgrade(self):
		print('1 - HP\n 2- DD\n 3 - MAX_HP')
		choice = input()
		if choice == '1':
			self.hp += 5
		elif choice == '2':
			self.dd += 2
		elif choice == '3':
			self.max_hp += 5
		else:
			self.upgrade()

		self.about()	

	def refresh(self):
		self.hp = self.max_hp

	def about(self):
		os.system('cls')
		print(f'Class - {self.role}\nDamage - {self.dd}\nHealth - {self.hp}\nMax HP - {self.max_hp}')

def create_hero():
	print('tank', 'dd', 'heal')
	role = input('choice your class:')
	if role == 'tank':
		hero = Hero('tank', 10, 100, 0, 100)
		return hero
	elif role == 'dd':
		hero = Hero('dd', 15, 80, 0, 80)
		return hero
	elif role == 'heal':
		hero = Hero('heal', 16, 70, 0, 70)
		return hero
	else:
		os.system('cls')
		print('Wrong class!\n')
		return 


class Enemy():

	def __init__(self, dd, hp):
		self.dd = dd
		self.hp = hp

	def about(self):
		print(f'Damage - {self.dd}, HP - {self.hp}\n')


def create_enemy():
	enemy = Enemy(random.randint(5,15), random.randint(90,110))
	return enemy