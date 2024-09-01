def calculate_factorial(n):

    if n == 0:
        return 1  # Factorial of 0 is 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Multiply factorial by each number from 1 to n
    return factorial 

print(calculate_factorial(5))
print(calculate_factorial(0))
print(calculate_factorial(7)) 
