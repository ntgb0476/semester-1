# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)

num_1 = input("Input your first number: ")
num_2 = input("Input your second number: ")

# multiply those numbers together

# if not num_1.isnumeric() or not num_2.isnumeric():
#     print("That is not a number")
#     exit()

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
except:
    print("That is not a number")
    exit()

result = int(num_1) * int(num_2)

# print out the result

print(result)

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!