# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()
if not numbers:
    sys.exit("Error: no numbers provided")
print(numbers)

sorted = numbers
sorted.sort()

maximum = sorted[-1]
minimum = sorted[0]
length = len(numbers)
mean = sum(numbers) / length
if not length % 2:
    median = (sorted[length // 2] + sorted[length // 2 - 1]) / 2
else:
    median = sorted[length // 2]

print(f"Minimum = {minimum}\nMaximum = {maximum}\nMean = {mean}\nMedian = {median}")
