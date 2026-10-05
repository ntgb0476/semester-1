"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

try:
    distance_miles = int(distance_miles_input)
except ValueError:
    print("That distance is not a valid number.")

try:
    time_hours_input = int(time_hours_input)
except ValueError:
    print("That time is not a valid number.")

average_speed = distance_miles / time_hours_input

print(f"To travel {distance_miles} miles in {time_hours_input} hours you must go {round(average_speed,2)} mph.")

# Extension: add validation for zero or negative values
