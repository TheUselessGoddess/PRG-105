"""
You need to create a program that will have the user enter the total sales amount for the day at a coffee shop.
The program should ask the user for the total amount of sales and include the day in the request.
At the end of data entry, tell the user the total sales for the week, and the average sales per day.
You must create a list of the days of the week for the user to step through, see the example output.
"""
total = 0.0
for x in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    total += float(input("What was the total amount of sales for " + x + "?"))

print("The total amount of sales for the week was: $" + str(format(total, '.2f')))
print("The average amount of sales per day was: $" + str(format(total / 7, '.2f')))
