import pandas as pd

# Create a DataFrame from a list
data_list = [['John', 28, 'Engineer'], ['Anna', 22, 'Doctor'], ['Mike', 32, 'Artist']]

# Specify the column names
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'Occupation'])

# Display the DataFrame created from the list
print("DataFrame created from List:")
print(df_list)

# Create a DataFrame from a dictionary
data_dict = {
    'Name': ['John', 'Anna', 'Mike'],
    'Age': [28, 22, 32],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
}

df_dict = pd.DataFrame(data_dict)

# Display the DataFrame created from the dictionary
print("\nDataFrame created from Dictionary:")
print(df_dict)
