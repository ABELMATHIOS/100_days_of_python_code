from calculator_art import logo
def add(n1 ,n2):
    return n1 + n2

def subtruct(n1 ,n2):
    return n1 - n2

def multiply(n1 ,n2):
    return n1 * n2

def divide(n1 ,n2):
    return n1 / n2

operation = {
    '+': add,
    '-': subtruct,
    '*': multiply,
    '/': divide,
}
def calculator():
    print(logo)
    num1 = float(input('what is the first number? '))
    for item in operation:
        print(item)
    not_end = True
    while not_end:
            symbol = input('pick an operation: ')
            num2 = float(input('what is the second number? '))
            calculation = operation[symbol]
            answer = calculation(num1, num2)
            print(f'{num1} {symbol} {num2} = {answer}')
            continue_playing = input(f"Type 'y' to continue calculating with {answer}, or type 'e' to exit or to start over a new calculation type 'n'.: ")
            if continue_playing == 'y':
                num1 = answer               
            else:
                not_end = False
                calculator()
calculator()

    
    
