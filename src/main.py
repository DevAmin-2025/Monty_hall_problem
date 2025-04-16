import random

from src.game_logic import eval_user_choice, simulate_game, winner_loser
from src.utils import print_info


if __name__ == '__main__':
	print_info('Welcome to Monty Hall program.\n')
	play = True

	while play:
		print('1. Simulation')
		print('2. Play\n')
		user_call = input('Please choose one of the options (q to exit): ')

		if user_call.lower() == 'q':
			print_info('Exiting the app...\n')
			break
		elif not user_call in ['1', '2']:
			print_info('Invalid input. Please Try again.\n')
			continue

		if user_call == '1':
			num_games = input('How many times do you want to repeat the simulation? (above 1000 for better results): ')
			try:
				num_games = int(num_games)
			except ValueError:
				print_info('Invalid input. We use the default value(10_000 times).\n')
				num_games = 10_000
			simulate_game(num_games)
		elif user_call == '2':
			print_info('There are 3 doors, behind two of them are goats and behind one of them is a car.')
			print_info("Let's see if you can win the car!")

			while True:
				doors = ['goat', 'goat', 'car']
				# Shuffling order of the doors each round
				random.shuffle(doors)
				user_choice = input('\nPlease choose door number 1, 2 or 3 (q to quit): ')

				if user_choice.lower() == 'q':
					print_info('Exiting the app...\n')
					play = False
					break
				elif not eval_user_choice(user_choice):
					continue

				user_choice = int(user_choice)
				# Reducing one to match doors list index
				user_choice -= 1

				# Possible doors to be revealed
				revealed_doors = [door for door in range(len(doors)) if door != user_choice and doors[door] != 'car']

				# Choosing one of the possible doors for reveling
				revealed_door = random.choice(revealed_doors)

				# Door if user want to change their initial door
				change_door = [door for door in range(len(doors)) if door != user_choice and door != revealed_door][0]

				# Adding one to the values to match the real door numbers
				print_info(f'Hint: Behind door number {revealed_door + 1} is a goat!')
				print_info(f'Now do you want to stick with door number {user_choice + 1} or you want to change it to door number {change_door + 1}?')

				user_decision = input(f'Enter {user_choice + 1} or {change_door + 1}: ')
				if user_decision != str(user_choice + 1) and user_decision != str(change_door + 1):
					print_info('\nInvalid input. Starting the game over...')
					continue
				winner_loser(user_decision, user_choice, change_door, doors)
