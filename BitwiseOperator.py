# Python program demonstrating different bitwise operators

# Initial values
a = 10  # In binary: 1010
b = 4   # In binary: 0100

print("a =", a, "-> Binary:", bin(a))
print("b =", b, "-> Binary:", bin(b))

# Bitwise AND
print("\nBitwise AND (a & b):")
print(f"{a} & {b} = {a & b} -> Binary: {bin(a & b)}")

# Bitwise OR
print("\nBitwise OR (a | b):")
print(f"{a} | {b} = {a | b} -> Binary: {bin(a | b)}")

# Bitwise XOR
print("\nBitwise XOR (a ^ b):")
print(f"{a} ^ {b} = {a ^ b} -> Binary: {bin(a ^ b)}")

# Bitwise NOT
print("\nBitwise NOT (~a):")
print(f"~{a} = {~a} -> Binary: {bin(~a)}")

# Left Shift
print("\nLeft Shift (a << 2):")
print(f"{a} << 2 = {a << 2} -> Binary: {bin(a << 2)}")

# Right Shift
print("\nRight Shift (a >> 2):")
print(f"{a} >> 2 = {a >> 2} -> Binary: {bin(a >> 2)}")
