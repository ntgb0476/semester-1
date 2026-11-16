import random

# Get user to input how many random numbers they want

number = int(input("How many random numbers do you want?: "))

# Generate this many random numbers

numbers = [str(random.randint(0, 100)) for x in range(number)]
print(numbers)

# Write the random numbers to a file named random.txt, one number per line

with open("random.txt", "w") as f:
    f.write("\n".join(numbers))
