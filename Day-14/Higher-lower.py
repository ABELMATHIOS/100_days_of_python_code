import random
from game_data import data
from art import logo, vs
import os

def game():
    score = 0
    def compare1():
        value1 = random.choice(data)
        return value1
    def compare2():
        value2 = random.choice(data)
        return value2
    x = compare1()
    y = compare2()
    is_not_game_over = True
    while is_not_game_over:
        print(logo)
        player1 = print(f"compare A: {x['name']}, {x['description']}, from {x['country']}.")
        print(vs)
        player2 = print(f"Against B: {y['name']}, {y['description']}, from {y['country']}.")
        ask  = input(f"who has more follower? ")
        if ask == 'a' and x['follower_count'] > y['follower_count']:
            score += 1 
            print(f"You're right! current score {score}.")
            data.remove(x)
            x = y
            os.system('cls')
        elif ask == 'b' and y['follower_count'] > x['follower_count']:
            score += 1
            print(f"You're right! current score {score}.")
            x = y
            os.system('cls')    
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            user = input("Do you want to play again, Type 'y' to play or press any key to exit. ")
            if user == 'y':
                os.system('cls')
                game()
            
            is_not_game_over = False
        y = compare2()             
game()

    
