import random
from src.utils import print_info, print_lose, print_win


def eval_user_choice(user_choice: str) -> bool:
	"""
	Evaluating user input according to specified criteria.

	:param user_choice: Input user choice.
	:return: True if input in validated, False otherwise.
	"""
	if not user_choice.isdigit() or not (3 >= int(user_choice) >= 1):
		print_info('\nInvalid input. You need to enter a number between one and three.')
		return False
	return True


def winner_loser(final_choice: str, user_choice: int, change_door: int, doors: list):
	"""
	Determine if the user wins or loses.

	:param final_choice: Input user choice.
	:param user_choice: Initial user choice (index).
	:param change_door: Door that can be switched to (index).
	:param doors: List of shuffled doors.
	"""
	final_choice = int(final_choice)

	if final_choice == (user_choice + 1):
		result = doors[user_choice]
		if result == 'goat':
			print_lose(f'\nYou lost! Behind door number {user_choice + 1} was a goat.')
		else:
			print_win(f'\nYou won the car!')
	elif final_choice == (change_door + 1):
		result = doors[change_door]
		if result == 'goat':
			print_lose(f'\nYou lost! Behind door number {change_door + 1} was a goat.')
		else:
			print_win(f'\nYou won the car!')


def monty_hall_game(switch_door: bool, doors: list = ['goat', 'goat', 'car']) -> bool:
	"""
	Play the Monty Hall game once, determining the outcome based on the choice to switch door or not.

	:param switch_door: True if switching the door, False otherwise.
	:param doors: List of doors.
	:return: True if behind the door is the car, False if a goat.
	"""
	# Shuffling order of the doors each time
	random.shuffle(doors)
	choice = random.choice(range(3))

	if switch_door is True:
		# Possible doors to be revealed
		revealed_doors = [door for door in range(3) if door != choice and doors[door] != 'car']
		# Choosing one of the possible doors for reveling
		revealed_door = random.choice(revealed_doors)
		# Door to be switched with user initial choice
		choice = [door for door in range(3) if door != choice and door != revealed_door][0]

	return doors[choice] == 'car'


def simulate_game(num_games: int):
	"""
	Simulate playing the Monty Hall game a specified number of times, both with and without switching doors.

	:param num_games: The number of games to simulate.
	"""
	wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
	wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])

	loses_w = num_games - wins_with_switching
	loses_wo = num_games - wins_without_switching
	percent_win_w = (wins_with_switching / num_games) * 100
	percent_lose_w = ((num_games - wins_with_switching) / num_games) * 100
	percent_win_wo = (wins_without_switching / num_games) * 100
	percent_lose_wo = ((num_games - wins_without_switching) / num_games) * 100

	print_info(
	f'With switching: {wins_with_switching:,} ({percent_win_w:.2f}%) wins'
	f' and {loses_w:,} ({percent_lose_w:.2f}%) losses out of {num_games:,} rounds.'
	)
	print_info(
		f'Without switching: {wins_without_switching:,} ({percent_win_wo:.2f}%) wins'
		f' and {loses_wo:,} ({percent_lose_wo:.2f}%) losses out of {num_games:,} rounds.\n'
	)
