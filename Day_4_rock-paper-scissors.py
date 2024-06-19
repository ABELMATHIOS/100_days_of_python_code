rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choice = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n'))
if user_choice >= 3 or user_choice <= 0:
    print('invalid number')
else:  
    print(choice[user_choice])
    computer_choice = random.randint(0,2)
    print(f'computer choose {computer_choice}')
    print(choice[computer_choice])

    if user_choice == 0 and computer_choice == 1:
        print('You lose!')
    elif user_choice == 1 and computer_choice == 0:
        print('You win!')
    elif user_choice == 0 and computer_choice == 2:
        print('You win!')
    elif user_choice == 2 and computer_choice == 0:
        print('You lose!')
    elif user_choice == 1 and computer_choice == 2:
        print('You lose!')
    elif user_choice == 2 and computer_choice == 1:
        print('You win!')
    elif user_choice ==  computer_choice:
        print('draw!')

