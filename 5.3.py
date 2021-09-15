"""
Create a menu function called from main that will present the user with the following menu.
This program will find the area of a shape for you.
1. Rectangle
2. Triangle
3. Square
4. Circle
5. Quit
Call a validation function from the main function to validate user input, use a while loop to validate data. Return the validated number to the main function.
Depending on the number selected, ask the user for the appropriate measurements to calculate the area of the specified shape (see the sample output)
 (Ask the user in the menu and pass the values to the called function)
Call the appropriate function, pass the required values to the function
Return the area to the main function and print it on screen from the main function
The menu should re-display until the user selects quit. Use a while loop in the main method with a flag to accomplish this.
Create a global variable for pi and use it when calculating the area of a circle.
"""
PI = 3.14
def validate(num):
    if 1 <= num <= 5:
        return True
    else:
        return False
def area_calc(selection):
    if selection == 1:
        length = float(input("Please enter the length of the rectangle."))
        height = float(input("Please enter the height of the rectangle."))
        return(format(length * height, '.2f'))
    if selection == 2:
        base = float(input("What is the length of the base of the triangle?"))
        height = float(input("What is the height of the triangle?"))
        return(str(format((base * height) / 2, '.2f')))
    if selection == 3:
        side = float(input("What is the length of one side of the square?"))
        return(str(format(side * side, '.2f')))
    if selection == 4:
        radius = float(input("What is the radius of the circle?"))
        return format((radius * radius) * PI, '.2f')

def menu():
    cont = True
    while cont == True:
        print("This program will find the area of a shape for you.\n1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit")
        number = int(input("Please enter the number of your selection:"))
        if validate(number) == True:
            if number == 5:
                cont = False
                print("Goodbye")
            elif number == 1:
                area = str(area_calc(number))
                print("The area of the rectangle is: " + area)
            elif number == 2:
                area = str(area_calc(number))
                print("The area of the triangle is: " + area)
            elif number == 3:
                area = str(area_calc(number))
                print("The area of the square is: " + area)
            elif number == 4:
                area = str(area_calc(number))
                print("The area of the circle is: " + area)
        else:
            print("That is not a valid number.")
menu()
