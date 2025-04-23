# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
print("\nUnion:", set1 | set2)  # or set1.union(set2)

# Intersection
print("Intersection:", set1 & set2)  # or set1.intersection(set2)

# Difference
print("Difference (Set1 - Set2):", set1 - set2)
print("Difference (Set2 - Set1):", set2 - set1)

# Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)  # or set1.symmetric_difference(set2)

# Subset and Superset
print("\nIs Set1 a subset of Set2?", set1.issubset(set2))
print("Is Set1 a superset of Set2?", set1.issuperset(set2))

# Disjoint Check
print("Are Set1 and Set2 disjoint?", set1.isdisjoint(set2))
