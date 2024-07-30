alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import sys
import cipher_art 
def caeser(plain_text, shift_amount, cipher_direction):
    cipher_text = ''
    for i in plain_text:
        if  i.isalpha():
            position = alphabet.index(i)
            if direction == 'encode':
                new_position = position + shift_amount
                
            elif direction == 'decode':
                new_position = position - shift_amount
            if shift > 26:
                new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            
            cipher_text += new_letter
        else:
              cipher_text += i  
        
    print(f"The {cipher_direction} text is {cipher_text}")




print(cipher_art.logo)

end_of_game = True
while end_of_game: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
            print("You have entered a wrong word. run the code again and read the instruction carefully.")
            sys.exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(plain_text=text, shift_amount=shift, cipher_direction=direction)

    again = input("Type 'yes' if you want to go again. otherwise type 'no'\n")
    if again == "no":
            end_of_game = False
            print("Goodbye")