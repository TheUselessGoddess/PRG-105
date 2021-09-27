"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test


days = ['Sunday', 'Monday', 'Tuesday', 'Wednseday', 'Thursday', 'Friday', 'Saturday']


# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
zero_list = [0] * 5
# 3) Print the contents of your days list using the for operator
for x in range(0, 7):
    print(days[x])
# 4) Print the list item that holds the value Saturday from the days list by using it's index
print(days[5])
# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)


# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days
work_days = days[1:6]
print(work_days)
# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)
# Test to see if "Tue" is in the list days - display "yes, Tue is in the list" or "no, Tue is not in the list"
if 'Tue' in days:
    print('yes, Tue is in the list')
else:
    print('no, Tue is not in the list')

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)
# 1) Use append() to append the last three months of the year to the list months.
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
months.append("October")
months.append("November")
months.append("December")
# 2) Get the index of "May" from the months list and print it on screen
print(months.index("May"))
# 3) Sort list3 from exercise 7.2 and print the results on screen
list3.sort()
print(list3)
# 4) Reverse the order of list3
list3.reverse()
# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
list3.remove(5)
print(list3)
# 6) Print the maximum value from list 3
print(max(list3))

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = months

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results
total = 0
for x in list3:
    total += x
print(total)
# 2) Get the average of values in list3 and print the results
total = 0
count = 0
for x in list3:
    total += x
    count += 1
print(total / count)
# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen
states = open('states.txt', 'r')
line = str(states.readline()).strip('\n')
states_list = [line]
while line != '':
    line = str(states.readline()).strip('\n')
    states_list.append(line)
print(states_list)
# TODO 7.8 Two-Dimensional Lists
print("=" * 10, "Section 7.8 two-dimensional lists", "=" * 10)
# 1) Create a new two dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31
year_times = [['January', '31'], ['February', '28'], ['March', '31'], ['April', '30'], ['May', '31'], ['June', '30'], ['July', '31'], ['August', '31'], ['September', '30'], ['October', '31'], ['November', '30'], ['December', '31']]
# 2) Print the contents of the entire list
print(year_times)
# 3) Print just the values for index 3,0 and 3,1
print(year_times[3][0])
print(year_times[3][1])
# TODO 7.9 Tuples
print("=" * 10, "Section 7.9 tuples", "=" * 10)
# Create a tuple using the months list as its data source
tuple_example = year_times

