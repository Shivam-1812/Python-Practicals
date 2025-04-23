# Program using different bitwise operators 
a = 10  # 1010 in binary 
b = 4   # 0100 in binary 
 
print("Bitwise AND:", a & b)   # 0000 = 0 
print("Bitwise OR:", a | b)    # 1110 = 14 
print("Bitwise XOR:", a ^ b)   # 1110 = 14 
print("Bitwise NOT:", ~a)      # -11 (2's complement) 
print("Left shift:", a << 2)   # 101000 = 40 
print("Right shift:", a >> 2)  # 0010 = 2