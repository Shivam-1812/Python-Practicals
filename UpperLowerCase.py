def count_case(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Original String:", text)
    print("Number of Uppercase letters:", upper_count)
    print("Number of Lowercase letters:", lower_count)

# Test the function
user_input = input("Enter a string: ")
count_case(user_input)
