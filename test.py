# def greet(name, location):
#     print(f"hello {name}")
#     print(f"your location is {location}")
# greet(name="abel", location="04street")
# import math
# def painting(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You will need {number_of_cans} of paint")

# test_h = int(input())
# test_w = int(input())
# coverage = 5
# painting(height=test_h, width=test_w, cover=coverage)
# def prime_checker(number):
#     for i in range(2, number):
#         num = True
#         if number % i == 0:
#             num = False
            
#     if num:
#         print('its a prime')
#     else:
#         print("not a prime")
# user = int(input())
# prime_checker(number=user)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher_ceaser(user_text, user_shift_num, user_direction):
    value = ""
    for item in text:
        if item in alphabet:
            legnth = len(alphabet)
            position = alphabet.index(item)
            new_shift = shift % legnth
            if direction == "encode":
                new_position = position + new_shift
            elif direction == "decode":
                new_position = position - new_shift       
            new_letter  = alphabet[new_position]
            value += new_letter
        else:
            value += item
        
    print(value)


end_of_game = True
while end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    cipher_ceaser(user_text=text, user_shift_num=shift, user_direction=direction)
    user_choice = input("type 'yes' if you want to continue otherwise 'no'\n")
    if user_choice == 'no':
        end_of_game = False






