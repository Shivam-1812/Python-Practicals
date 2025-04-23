# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Display the original list
print("Original List:", fruits)

# append() - add an item to the end
fruits.append("orange")
print("After append():", fruits)

# insert() - insert item at a specific position
fruits.insert(2, "grape")
print("After insert():", fruits)

# remove() - remove a specific item
fruits.remove("banana")
print("After remove():", fruits)

# pop() - remove item at a specific index (or last if no index is given)
fruits.pop()
print("After pop():", fruits)

# index() - get the index of a value
index_of_mango = fruits.index("mango")
print("Index of 'mango':", index_of_mango)

# count() - count occurrences of an item
count_apple = fruits.count("apple")
print("Count of 'apple':", count_apple)

# sort() - sort the list in ascending order
fruits.sort()
print("After sort():", fruits)

# reverse() - reverse the list
fruits.reverse()
print("After reverse():", fruits)

# clear() - remove all items from the list
fruits.clear()
print("After clear():", fruits)
