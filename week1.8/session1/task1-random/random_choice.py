import random

# Read names from a file

with open("names.txt") as infile:
    names = [line.strip() for line in infile]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

number = int(input("Number of random names: "))
chosen_names = random.sample(names, number)

# Display the chosen names, one per line

print(chosen_names)
