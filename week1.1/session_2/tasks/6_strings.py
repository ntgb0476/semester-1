# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

# Prints the orginal string
print(f"\nOriginal String: {user_string}")

# Prints the string with every letter lowercase
print(f"Modified String 1: {user_string.lower()}")

# Prints the string with every letter upper case
print(f"Modified String 2: {user_string.upper()}")

# Prints the string without any whitespace around it
print(f"Modified String 3: {user_string.strip()}")

# Replaces every instance of a with @
print(f"Modified String 4: {user_string.replace('a', '@')}")

# Prints the string with the first letter capitalized
print(f"Modified String 5: {user_string.capitalize()}")

# Prints the string backwards. This uses string slicing with a step of minus one
print(f"Modified String 6: {user_string[::-1]}")

# Prints the string in title case(The start of every word is capilaized)
print(f"Modified String 7: {user_string.title()}")

# Prints the length of the string
print(f"Modified String 8: {len(user_string)}")

# Prints the index of the first letter a's
print(f"Modified String 9: {user_string.find('a')}")

# Prints the number of letter a's in the string
print(f"Modified String 10: {user_string.count('a')}")

# Prints True if the string starts with "Hello"
print(f"Modified String 11: {user_string.startswith('Hello')}")

# Prints True if the string ends with "!"
print(f"Modified String 12: {user_string.endswith('!')}")

# Prints True if all characters are alphanumeric
print(f"Modified String 13: {user_string.isalnum()}")

# Prints True if all the characters are alpha letters
print(f"Modified String 14: {user_string.isalpha()}")

# Prints True if all the charaters are numbers
print(f"Modified String 15: {user_string.isdigit()}")

######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!