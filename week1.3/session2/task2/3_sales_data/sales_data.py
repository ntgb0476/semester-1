# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows

with open("sales.csv") as f:
    file = f.read()

file = file.split("\n")

days = {}

for line_number in range(len(file)):
    line = file[line_number]
    values = line.split(",")
    if line_number == 0:
        headers = values
    else:
        days.update({values[0]: {headers[n]: values[n] for n in range(len(headers))}})


sales = [day["Sales_Amount"] for (date, day) in days.items()]

max_sales = 0
widgets = {}
all_sales = []
for date, day in days.items():
    if int(day["Sales_Amount"]) > int(max_sales):
        max_sales = day["Sales_Amount"]
        max_sales_date = date
    widgets[day["Product"]] = int(widgets.get(day["Product"], 0)) + int(
        day["Sales_Amount"]
    )
    all_sales.append(int(day["Sales_Amount"]))

print(sum(all_sales) / len(all_sales))

print(max(widgets))

print(widgets)
print(f"Max sales({max_sales}) on {max_sales_date}.")
