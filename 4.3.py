"""
Write a program that projects yearly income, the amount saved towards retirement each year, and total retirement savings.
Assume a 3 percent raise on the starting income each year, and a 6% yearly return on investment.
You will need to ask the user their current age, at what age they want to retire, what their current income is,
what percent of their income they save each year, and how much they currently have in savings.
You will calculate how many years until retirement, and display the projected income, savings contribution, and total savings each year.
"""


income = float(input("What is your current yearly income?"))
savings_percent = float(input("What percentage of your income do you save each year?")) / 100
total_savings = float(input("What is your current total savings?"))
age = int(input("What is your current age?"))
age2 = int(input("At what age do you wish to retire?"))
year = 0
print("This projection assumes a 3% raise each year and a 6% yearly return on investment.")
print("Year                  Income                    Savings Contribution                  Total Savings")
for x in range(age, age2):
    year += 1
    if year < 10:
        print("  " + str(year) + format(round(income), '25,d') + format(round(income * savings_percent), '40,d') + format(round(total_savings), '32,d'))
    else:
        print(" " + str(year) + format(round(income), '25,d') + format(round(income * savings_percent), '40,d') + format(round(total_savings), '32,d'))
    income = income * 1.03
    contribution = income * savings_percent
    total_savings = total_savings * 1.06
    total_savings += contribution


