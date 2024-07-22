from blind_acution_art import logo
from os import system
print(logo)
bidder = {}
def bidder_game(user_name, user_bid):
        bidder[user_name] = user_bid
end_of_bid = True
while  end_of_bid:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: '))
    bidder_game(user_name=name, user_bid=bid)
    new_bidder = input("Are there any other bidder? Type 'yes' or 'no'.: ")
    system('cls')
    if new_bidder == 'no':
        end_of_bid = False
val = 0
for item in bidder:
    x = bidder[item]
    if x > val:
        val = x
print(f'The winner is {name} with a bid of ${bid}.')





    
