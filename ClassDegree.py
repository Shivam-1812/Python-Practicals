# Base Class
class Degree:
    def getDegree(self):
        print("I got a degree")

# Subclass of Degree
class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

# Subclass of Degree
class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")

# Creating objects of each class
degree = Degree()
undergraduate = Undergraduate()
postgraduate = Postgraduate()

# Calling the getDegree method for each object
degree.getDegree()           # Output: I got a degree
undergraduate.getDegree()    # Output: I am an Undergraduate
postgraduate.getDegree()     # Output: I am a Postgraduate
