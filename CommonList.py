# Define two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# Find common elements using list comprehension and set
common_items = list(set(list1) & set(list2))

# Print the result
print("List 1:", list1)
print("List 2:", list2)
print("Common items:", common_items)
