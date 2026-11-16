#!/usr/sbin/uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pandas",
# ]
# ///

import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(data)

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students

print(len(data))

# Find the mean average GPA of the students

print(data.loc[:, "GPA"].mean())

# Find the standard deviation of how much sleep students get per day

print(data.loc[:, "Sleep_Hours_Per_Day"].std())

# Find the maximum amount of study hours per day

print(data.loc[:, "Study_Hours_Per_Day"].max())

# Sort the students by social hours per day ascending (lowest -> highest)

data = data.sort_values("Social_Hours_Per_Day")
print(data)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
categories = [
    "Study_Hours_Per_Day",
    "Extracurricular_Hours_Per_Day",
    "Sleep_Hours_Per_Day",
    "Social_Hours_Per_Day",
    "Physical_Activity_Hours_Per_Day",
]

data["Total_Hours"] = 0

for category in categories:
    data["Total_Hours"] = data[category] + data["Total_Hours"]

print(data)

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?

print(
    "High Stress :",
    data.filter(pandas.col("Stress_Level") == "High").loc[:, "GPA"].mean(),
    data.filter(pandas.col("Stress_Level") == "High").loc[:, "GPA"].std(),
)
print(
    "Moderate Stress :",
    data.filter(pandas.col("Stress_Level") == "Moderate").loc[:, "GPA"].mean(),
    data.filter(pandas.col("Stress_Level") == "Moderate").loc[:, "GPA"].std(),
)
print(
    "Low Stress :",
    data.filter(pandas.col("Stress_Level") == "Low").loc[:, "GPA"].mean(),
    data.filter(pandas.col("Stress_Level") == "Low").loc[:, "GPA"].std(),
)
