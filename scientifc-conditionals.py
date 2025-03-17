def fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fib_series = [0, 1]  # Initial values
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    print("Fibonacci sequence:", *fib_series[:n])

nterms = int(input("How many terms? "))
fibonacci_series(nterms)
# How many terms? 5
# Fibonacci sequence: 0 1 1 2 3


def is_armstrong(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_digits

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# Enter a number: 153
# 153 is an Armstrong number.

# Enter a number: 1253
# 1253 is not an Armstrong number.

def reverse_number(n):
    return int(str(n)[::-1])

def find_palindrome(n):
    while True:
        rev = reverse_number(n)
        if n == rev:
            return n
        n += rev

num = int(input("Enter a number: "))
palindrome = find_palindrome(num)
print(f"Palindrome number is {palindrome}")

# Enter a number: 145
# Palindrome number is 686

# Enter a number: 144
# Palindrome number is 585
