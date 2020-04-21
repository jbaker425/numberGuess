from random import seed, randint
from time import time

def validInput(inp, beg, end):
	#Check if integer
	try:
		int(inp)
	except ValueError:
		print("\n-------------------------\nInvalid input. Try Again\n-------------------------\n")
		print("\nWrong data type, please use an integer.\n")
		return False
	else:
		#Check if in range
		if int(inp) < beg:
			print("\n-------------------------\nInvalid input. Try Again\n-------------------------\n")
			print("\nYour input was too low.\n")
			return False
		elif int(inp) > end:
			print("\n-------------------------\nInvalid input. Try Again\n-------------------------\n")
			print("\nYour input was too high\n")
			return False
		else:
			return True

if __name__ == '__main__':
	
	while True:
		# main program
		seed(time())
		ans = randint(1,256)
		guess = -1
		attempts = 0
		MAXATTEMPTS = 8

		while guess != ans and attempts < MAXATTEMPTS:
			noun = 'guesses'
			if attempts == MAXATTEMPTS - 1:
				noun = noun[:-2]
			print(f"You have {MAXATTEMPTS-attempts} {noun}.")
			guess = input("Enter a number between 1 and 256 ('q' to quit): ")
			if guess in ('q', 'Q', 'quit', 'Quit', 'QUIT'):
				print("Exiting game ...")
				break
			elif validInput(guess, 1, 256):
				guess = int(guess)
				attempts += 1
				if guess > ans:
					print("The answer is lower than", guess)
				elif guess < ans:
					print("The answer is higher than", guess)
				else:
					print("You got it! The number was", guess)
					break

		if attempts == MAXATTEMPTS and guess != ans:
			print("Sorry you ran out of guesses.")

		while True:
			answer = input('Run again? (y/n): ')
			if answer in ('y', 'n'):
				break
			print('Invalid input.')
		if answer == 'y':
			continue
		else:
			print('Goodbye')
			break




