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
print("what do you choose? Type 0 for rock, 1 paper, 2 for scissors.")
choice = [rock, paper, scissors]
p1 = int(input())
if p1 >= 3 or p1 < 0:
    print('invalid number')
else:
    print(choice[p1])
    cc =(random.randint(0,2))
    print('comupter choose:')
    print(choice[cc])


    if p1 == 0 and cc == 1:
        print('computer win!')
    elif p1 == 1 and cc == 0:
        print('you win!')
    elif p1 == 0 and cc == 2:
        print('you win!')
    elif p1 == 2 and cc == 0:
        print('computer win!')
    elif p1 == 2 and cc == 1:
        print('you win!')
    elif p1 == 1 and cc == 2:
        print('computer win!')
    elif p1 == cc:
        print('draw')

    else:
        print('you have entered a wrong number')









