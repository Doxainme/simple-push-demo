def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
except ValueError:
    print("Please enter a valid integer.")
