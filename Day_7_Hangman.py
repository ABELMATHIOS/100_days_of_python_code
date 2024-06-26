import random
import os
from  hangman_art import logo, stages
from hangman_words import word_list

random_choice = random.choice(word_list)
print(random_choice)
display = []
for i in range(len(random_choice)):
  display += "_"
lives = 6
a = 3
print(logo)
while a > 1:
  guess = input("Guess a letter: ").lower()
  os.system('cls')
  if guess in display:
    print(f"You've already guessed the letter {guess}.")
  for i in range(len(random_choice)):
    letter = random_choice[i]
    if letter == guess:
      display[i] = letter
  if guess not in random_choice:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      a = 0
      print('You lose!')

  if "_" not in display:
    a = 0
    print("You win!")

  
  string = ''.join(display)
  print(string)
   
  print(stages[lives]) 