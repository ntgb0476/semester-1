# Week 1.3, Session 1: Task 1b

fruit = ["apple", "pear", "banana", "orange"]

# loop through the list
while fruit:
    print(fruit.pop())


# Why does this work?
# It pops the last item off the list and prints it. Popping removes the item from the list. It repeats this until the list is empty.

# What features of Python does it rely on?
# Lists have a built in .pop() function and return False if they are empty or True if not empty.

