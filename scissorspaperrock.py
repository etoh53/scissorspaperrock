from random import choice

user_input_list = ("scissors", "paper", "stone")

# How many rounds to loop
def get_round_loop_count():
	round_prompt_repeat = True
	while round_prompt_repeat == True:
		try:
			round_count = int(input("How many games do you want to play in a round?\n"))
		except:
			print("Please enter a valid fucking number.")
		else:
			if round_count < 1:
				print("Please enter a number greater than 0.")
			else:
				round_prompt_repeat = False
				return round_count

# User input what
def get_user_input():
	input_prompt_repeat = True
	while input_prompt_repeat == True:
		user_input = input("Scissors paper stone!\n").lower()
		if user_input not in user_input_list:
			print("Please enter a valid input so we do not ruin the whole immersion of the game, not that the immersion has not already been ruined.")
		else:
			input_prompt_repeat = False
			return user_input

# Computer choose
def computer_choose():
	computer_choice = choice(user_input_list)
	return computer_choice

# Game logic
def logic(user_input_arg, computer_choice_arg):
	a = user_input_arg
	b = computer_choice_arg
	if (a == "scissors" and b == "paper") or (a == "paper" and b == "stone") or (a == "stone" and b == "scissors"):
		outcome = "win"
	else:
		outcome = "lose"
	return outcome

# Main game function
def main():
	play_again = True
	while play_again == True:
		win_count = 0
		round_loop_count = get_round_loop_count()	
		for round_count in range(0, round_loop_count):
			user_input = get_user_input()
			computer_choice = computer_choose()
			game_outcome = logic(user_input, computer_choice)
			if game_outcome == "win":
				print("Congratulations, you won this round!")
				win_count += 1
			else:
				print("Unfortunately, you lost this round.")
		percentage_score = round(((win_count / round_loop_count) * 100), 1)
		print("You won " + str(win_count) + " time(s). Your percentage score is " + str(percentage_score) + "%.")
		try_again = input("Do you want to try again?\n").lower()
		repeat = True
		while repeat == True:
			if try_again == "no" or try_again == "n":
				play_again = False
				repeat = False
				exit()
			elif try_again == "yes" or try_again == "y":
				repeat = False
			else:
				print("Please enter a correct value.")

if __name__ == "__main__":
	main()