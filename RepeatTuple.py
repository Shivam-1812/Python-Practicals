# Sample tuple
sample_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 2, 7)

# Create an empty list to store duplicates
repeated_items = []

# Loop through each item and check for multiple occurrences
for item in sample_tuple:
    if sample_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

# Display results
print("Original Tuple:", sample_tuple)
print("Repeated Items:", tuple(repeated_items))
