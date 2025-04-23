# First row (7 characters)
for i in range(1, 8):
    print(i % 2, end="")
print()

# Second row (3 characters, centered)
print("  ", end="")  # 2 spaces
for i in range(1, 4):
    print(i % 2, end="")
print()

# Third row (1 character, centered)
print("   1")
