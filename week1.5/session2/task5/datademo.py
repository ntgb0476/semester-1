# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

from data import Dataset

dataset = Dataset("data.txt")

print(len(dataset))
print(dataset)
print(dataset.mean())
print(dataset[2])
print(dataset.median())
