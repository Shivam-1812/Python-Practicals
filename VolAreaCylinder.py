import math

# Input from user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculations
volume = math.pi * radius**2 * height
surface_area = 2 * math.pi * radius * (radius + height)

# Output
print(f"\nVolume of the cylinder = {volume:.2f}")
print(f"Surface Area of the cylinder = {surface_area:.2f}")
