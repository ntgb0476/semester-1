"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jonathan Buss
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

monthy_payed_in = input("Input amount you will pay in each month: ")

try:
    monthy_payed_in = int(monthy_payed_in)
except:
    print(f"{monthy_payed_in} is not a vaild number.")
    exit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearly = monthy_payed_in * 12

print(f"You will be saving {yearly} over the whole year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest = yearly * 0.008

total = yearly + interest

round = "%.2f" % round(total, 2)
# trailing zero lifted from:
# https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros

print(f"At the end of the year your balance will be £{round}")