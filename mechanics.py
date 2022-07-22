import random
from entities import *
import os


def game():
	while True:
		hero = create_hero()
		if hero:
			break

	while True:	

		os.system('cls')	
		choice = choice_menu()
		
		if choice == 'Fight':
			enemy = create_enemy()

			while True:				
				res = fight(hero, enemy)
				if res == 'win':
					hero.upgrade()
					hero.refresh()
					break
				elif res == 'lose':
					return 'Quit'
				elif res == 'Quit fight':
					break
				else:
					print('Try again')
					
		elif choice == 'Stats':

			hero.about()
			input('press any button')

		elif choice == 'Quit':
			return 'Quit'

		else:
			print('Try again')

def choice_menu():
	print('Menu')
	print('1. Fight')
	print('2. Check stats')
	print('3. Quit')
	choice = input()

	if choice == '1':
		return 'Fight'
	elif choice == '2':
		return 'Stats'
	elif choice == '3':
		return 'Quit'
	else:
		return 'Error'	

def fight(hero,enemy):
	os.system('cls')  
	r = random.randint(1,2)
	print('Enemy')
	enemy.about()
	print('You')
	print(f'Damage - {hero.dd}, HP - {hero.hp}\n')
	print('Your choice\n')
	print('1. Punch')
	print('2. Quit')

	n = input('Choice:')
	if n == "1":

		enemy.hp -= hero.dd
		print(f'You deal {hero.dd} damage!')
		hero.hp -= enemy.dd
		print(f'Enemy deal {enemy.dd} damage!\n')
		
		if hero.hp <= 0:
			print('you lose')
			return 'lose'
		if enemy.hp <= 0:
			print('you win')
			return 'win'

	if n == "2":
		return 'Quit fight'