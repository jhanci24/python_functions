def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Generate the first 10 Fibonacci numbers
fibonacci_sequence = fibonacci(10)
print("Fibonacci Sequence:", fibonacci_sequence)

'''
This function, fibonacci, generates the Fibonacci sequence up to a specified number n using recursion.
'''