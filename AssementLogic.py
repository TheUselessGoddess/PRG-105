"""
Create a program that helps someone create a budget. It should ask the user for monthly income and the following expenses:

Housing
Food
Transportation
Phone
Utilities
Clothing

The program should get input from the user and convert each of the inputs to floats.
The program should tell the user how much money they have left after they have paid all of their bills.
The program should calculate and display the income percentage of each budget item.
"""
income = float(input("What is your monthly income amount?"))
housing = float(input("How much do you spend on housing each month?"))
food = float(input("How much do you spend on food each month?"))
transportation = float(input("How much do you spend on transportation each month?"))
phone = float(input("How much do you spend on a phone each month?"))
utilities = float(input("How much do you spend on utilities each month?"))
clothing = float(input("How much do you spend on clothing each month?"))
end_income = income

print("Housing takes up " + str(format((housing / income), '.2%')) + " of your budget.")
end_income = end_income - housing
print("Food takes up " + str(format((food / income), '.2%')) + " of your budget.")
end_income = end_income - food
print("Transportation takes up " + str(format((transportation / income), '.2%')) + " of your budget.")
end_income = end_income - transportation
print("Phone bill takes up " + str(format((phone / income), '.2%')) + " of your budget.")
end_income = end_income - phone
print("Utilities takes up " + str(format((utilities / income), '.2%')) + " of your budget.")
end_income = end_income - utilities
print("Clothing takes up " + str(format((clothing / income), '.2%')) + " of your budget.")
end_income = end_income - clothing
print("You have $" + str(end_income) + " left from your income after paying these monthly expenses.")
