# This is a solution to problem 15 of Assignment 01 - Welcome to FP

def is_perfect(x):
    SumOfDivisors = 0
    for i in range(1,x):
        if x % i == 0:
            SumOfDivisors += i

    return SumOfDivisors == x

def biggest_perfect_number_smaller_than(n):
    for x in range(n-1, 1, -1):
        if is_perfect(x):
            return x

    return -1

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

answer= biggest_perfect_number_smaller_than(n)

if answer == -1:
    print("No such number exists.")
else:
    print(f"The biggest perfect number smaller than {n} is {answer}.")