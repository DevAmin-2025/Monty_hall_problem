# Monty Hall Game and Simulation

## Description
This Python project simulates the classic Monty Hall problem, a probability puzzle based on a game show scenario. The game involves three doors: behind one door is a car, and behind the other two doors are goats. The player initially chooses one door, and then the host reveals a goat behind one of the other two doors. The player then has the option to stick with their original choice oe switch to the remaining unopened door. This project allows users to play the game or simulate multiple rounds to analyze the probabilities.

## Modules
The project is divided into three main modules:

### `utils.py`
Contains helper functions for printing messages:
- `print_info(text: str)`: Prints an informational message.
- `print_lose(text: str)`: Prints a losing message.
- `print_win(text: str)`: Prints a winning message.

### `game_logic.py`
Contanis the core game logic functions:
- `eval_user_choice(user_choice: str)`: Evaluates the user's input.
- `winner_loser(final_choice: str, user_choice: int, change_door: int, doors: list)`: Determines if the user wins or loses.
- `monty_hall_game(switch_door: bool, doors: list)`: Simulates one round of the Monty Hall game.
- `simulate_game(num_games: int)`: Simulates multiple rounds of the Monty Hall game.

### `main.py`
Contains the main entry point of the application with user interaction.

## Game Options
1. **Simulation**: Simulate multiple rounds of the Monty Hall game to analyze the probabilities.
2. **Play**: Play the Monty Hall game interactively.

## How to Run
Tor run the application, follow these steps:
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Navigate to the main project directory.
```bash
cd Monty_hall_problem
```
3. Add the current directory to the `PYTHONPATH` and run the `main.py` script.
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
3. Install any necessary dependencies:
```bash
pip install -r requirements.txt
```
