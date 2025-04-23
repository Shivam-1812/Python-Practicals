# Input from user
n = int(input("Enter the number of terms in Fibonacci series: "))

# First two terms
a, b = 0, 1
count = 0

print("Fibonacci Series:")

# Generate Fibonacci series
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
