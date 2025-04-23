# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate all dictionaries
merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)

# Display the new merged dictionary
print("Concatenated Dictionary:", merged_dict)
