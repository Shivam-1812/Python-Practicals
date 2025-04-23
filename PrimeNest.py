print("Prime numbers from 2 to 100 are:")

for num in range(2, 101):  # Numbers from 2 to 100
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
