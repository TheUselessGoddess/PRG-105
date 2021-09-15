"""
Write a program that asks a user to enter a whole number between 20 and 100.
Send that number to a function that will validate the number, and if it is not a number between 20 and 100,
 use a while loop to keep asking the user for a valid number. Return the number to the main function
 (hint good_number = validate(num) - use a variable to store the returned value).

You will also program three functions that determine if the number is divisible by two, by three, and by five.

You will have a final function that puts output on the screen - identifying if the number is divisible by two, three, and five.
"""
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
def validate_num(num):
    if 20 <= num <= 100:
        return True
    else:
        return False



def final():
    good_number = False
    while good_number == False:
        number = int(input("Enter a whole number between 20 and 100."))
        good_number = validate_num(number)
        if good_number == True:
            div2(number)
            div3(number)
            div5(number)
final()
