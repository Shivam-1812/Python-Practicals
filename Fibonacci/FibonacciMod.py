# main.py
import fibonacci_module

# Take input from the user for the number of Fibonacci numbers to display
num = int(input("Enter the number of Fibonacci numbers to display: "))

# Call the function from the fibonacci_module
fib_numbers = fibonacci_module.fibonacci(num)

# Display the Fibonacci sequence
print(f"The first {num} Fibonacci numbers are:", fib_numbers)
