d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined = d1.copy()
for key, value in d2.items():
    if key in combined:
        combined[key] += value
    else:
        combined[key] = value
print(combined)  # Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}