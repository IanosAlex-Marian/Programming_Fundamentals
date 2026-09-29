# This is a solution to problem 7 of Assignment 01 - Welcome to FP

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    
    return True

def twin_primes_greater_than(n):
    current_number= n + 1
    while True:
        if is_prime(current_number) and is_prime(current_number + 2):
            return (current_number, current_number + 2)
        
        current_number += 1

def read_natural_number():
    while True:
        try:
            n = int(input("Enter a natural number: "))

            if n <= 0:
                print("Please enter a natural number greater than 0.")
            else:
                return n

        except ValueError:
            print("Please enter a valid number.")

n = read_natural_number()
answer= twin_primes_greater_than(n)

print(f"The first twin primes greater than {n} are {answer[0]} and {answer[1]}.")