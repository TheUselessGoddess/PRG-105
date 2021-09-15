"""
Write a program that asks a user to enter a whole number between 20 and 100.
Send that number to a function that will validate the number, and if it is not a number between 20 and 100,
 use a while loop to keep asking the user for a valid number. Return the number to the main function
 (hint good_number = validate(num) - use a variable to store the returned value).

You will also program three functions that determine if the number is divisible by two, by three, and by five.

You will have a final function that puts output on the screen - identifying if the number is divisible by two, three, and five.
"""
number = 0
def validate(num):
    print()

def div2(num):
    if num % 2 == 0:
        print(str(num) + " is divisible by 2")
    else:
        print(str(num) + " isn't divisible by 2")
def div3(num):
    if num % 3 == 0:
        print(str(num) + " is divisible by 3")
    else:
        print(str(num) + " isn't divisible by 3")
def div5(num):
    if num % 5 == 0:
        print(str(num) + " is divisible by 5")
    else:
        print(str(num) + " isn't divisible by 5")
while number < 20 or number > 100:
    number = int(input("Enter a whole number between 20 and 100."))
    if 20 <= number <= 100:
        div2(number)
        div3(number)
        div5(number)
