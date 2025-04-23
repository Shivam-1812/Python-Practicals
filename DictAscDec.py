# Sample dictionary
my_dict = {'apple': 40, 'banana': 10, 'mango': 30, 'grapes': 20}

# Sort dictionary by values in ascending order
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", asc_sorted)

# Sort dictionary by values in descending order
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", desc_sorted)
