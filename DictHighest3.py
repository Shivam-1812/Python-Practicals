# Sample dictionary
my_dict = {'a': 50, 'b': 150, 'c': 300, 'd': 200, 'e': 100}

# Sort the dictionary by values in descending order and get top 3 items
top_3 = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3]

# Display the result
print("Top 3 highest values in the dictionary:")
for key, value in top_3:
    print(f"{key}: {value}")
