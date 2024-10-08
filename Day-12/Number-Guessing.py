from art import logo
import random
print(logo)
EASY_LEVEL = 10
HARD_LEVEL = 5

print("Welcome to the Number Guessing Game!")
print("I'am thinking of a number between 1 and 100.")
difficulty =  input("Choose difficulty. Type 'easy' or 'hard' ")
rand_num = random.randint(1, 100)
def game():
    def number_guessing(guess, rand_num, turns):
        if guess < rand_num:
            print('Too low.')
            turns = turns - 1
            return turns
        elif guess > rand_num:
            print('Too high')
            returns = turns - 1
            return turns
        elif guess == rand_num:
            print(f'You got it! The answer was {guess}')
        return turns
   
    def set_difficulty():
        if difficulty == 'easy':
            turns = EASY_LEVEL
            return turns
        elif difficulty == 'hard':
            turns = HARD_LEVEL
            return turns
    turns = set_difficulty()
    guess = 0  
    while guess != rand_num:
        print(f"You have {turns} attempts remaining to guess the number.")
    
        guess = int(input('Make a guess: '))
        turns = number_guessing(guess,rand_num,turns)
        if turns == 0:
            print('You are out of guesses, You lose')
            return
game()