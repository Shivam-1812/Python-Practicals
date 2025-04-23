# Step 1: Create an empty set
my_set = set()
print("Initial Set:", my_set)

# Step 2: Add members to the set
my_set.add(10)
my_set.add(20)
my_set.add(30)
print("Set after adding elements:", my_set)

# Step 3: Add multiple items at once
my_set.update([40, 50])
print("Set after adding multiple items:", my_set)

# Step 4: Remove an item from the set
my_set.remove(20)
print("Set after removing 20:", my_set)
