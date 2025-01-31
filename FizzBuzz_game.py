#The loop will run until the user decides to exit.
while True:
    user_input = input("Enter any natural number: ")

    #checks if the input is a natural number, if not
    # Skip the rest of the code inside the loop for the current iteration and start the next iteration of the loop immediately.
    if not user_input.isdigit():
        print("You have entered an invalid input. Please enter a valid natural number.")
        continue

    # It converts the string input to integer.
    user_input = int(user_input)
    # Perform FizzBuzz logic on the single number
    if user_input % 3 == 0 and user_input % 5 == 0:
        print('FizzBuzz')
    elif user_input % 3 == 0:
        print('Fizz')
    elif user_input % 5 == 0:
        print('Buzz')
    else:
        print(f"The number {user_input} is not divisible by 3 or 5.")

    # Ask if the user wants to play again.
    play_again = input("Would you like to play again? Type 'y' for yes or press any key to exit: ").lower()
    if play_again != 'y':
        print("Thanks for playing our game.")
        #Exit the loop
        break