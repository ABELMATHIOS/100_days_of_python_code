import blind_acution_art
import os
import sys
print(blind_acution_art.logo)
print("Welcome to the secret auction program.")
auction = {}

def finished(b_auction):
    highest_value = 0 
    for value in auction:
        a = auction[value]
        if a > highest_value:
            highest_value = a
            print(f"The winner is {value} with a bid of ${highest_value}.")
    
    
end_of_game = True
while end_of_game:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] =bid
    bidders = input("Are there any other bidders? 'yes' or 'no'.\n")
    if bidders == "no":
        end_of_game = False
        finished(auction)
    elif bidders == "yes":
        os.system('cls')
    else:
        print("You typed the incorrect word. Run the code once more while carefully reading the instructions.")
        sys.exit()

