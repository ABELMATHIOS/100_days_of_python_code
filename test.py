number = int(input('enter a number'))
def is_prime(num):
    if num % num == 0 and num % 1 == 0:
        return True
    else:
        return False
        

print(is_prime(number))