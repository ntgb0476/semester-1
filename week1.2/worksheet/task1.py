# Worksheet 1.2: Task 1 Solution
try:
    grade = int(input("Input a grade: "))
except:
    raise Exception("Error: Grade must be an integer between 0 and 100")

if 0 <= grade < 40:
    print(f"{grade} is a Fail")
elif 40 <= grade < 70:
    print(f"{grade} is a Pass")
elif 70 <= grade <= 100:
    print(f"{grade} is a Distinction")
else:
    raise Exception("Error: Grade must be an integer between 0 and 100")