# Factorial

def factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: multiply n by factorial of (n-1)
    return n * factorial(n-1)

# Example usage: calculate factorial of 4 and print the result
print(factorial(4))
