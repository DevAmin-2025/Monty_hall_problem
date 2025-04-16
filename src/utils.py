'''
Provide defferent ways to have colorful prints.
'''
from termcolor import colored


def print_info(text):
	print(colored(text, 'white', attrs=['reverse']))


def print_win(text):
	print(colored(text, 'green', attrs=['reverse']))


def print_lose(text):
	print(colored(text, 'red', attrs=['reverse']))
