import pandas as pd
import numpy as np

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Convert NumPy array to Pandas Series
series = pd.Series(data)

# Display the series
print("Pandas Series from NumPy Array:")
print(series)
