# This is a solution to problem 1 of Assignment 01 - Welcome to FP

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    
    return True

def first_prime_greater_than(n):
    current_number= n + 1
    while True:
        if is_prime(current_number):
            return current_number
        
        current_number += 1

def read_natural_number():
    while True:
        try:
            n = int(input("Enter a natural number: "))

            if n < 0:
                print("Please enter a natural number (0 or greater).")
            else:
                return n

        except ValueError:
            print("Please enter a valid integer.")

n = read_natural_number()

print(f"The first prime number greater than {n} is {first_prime_greater_than(n)}.")