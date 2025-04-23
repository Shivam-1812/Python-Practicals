import pandas as pd

# Create a Series with custom indexes
my_series = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])

# Display the Series
print("Full Series:")
print(my_series)

# Accessing elements using index labels
print("\nElement at index 'b':", my_series['b'])

# Accessing elements using integer positions (correct way)
print("Element at position 2:", my_series.iloc[2])

# Accessing multiple elements using a list of labels
print("\nElements at index 'a', 'c', and 'e':")
print(my_series[['a', 'c', 'e']])
