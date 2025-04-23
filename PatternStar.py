rows = 3  # Number of rows in the top half

# Top half of the diamond
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Bottom half of the diamond
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
