class Shape:
    # Method to calculate the area of square
    def area(self, side=None, length=None, breadth=None):
        if side is not None:
            # Calculate area of square
            return side * side
        elif length is not None and breadth is not None:
            # Calculate area of rectangle
            return length * breadth
        else:
            return "Invalid parameters"

# Creating object of Shape class
shape = Shape()

# Calling the method to calculate area of square
square_area = shape.area(side=5)
print(f"Area of square: {square_area}")

# Calling the method to calculate area of rectangle
rectangle_area = shape.area(length=4, breadth=6)
print(f"Area of rectangle: {rectangle_area}")
