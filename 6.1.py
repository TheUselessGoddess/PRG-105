"""
Write a program that gathers contact information from people.
The program should ask the user how many entries they are going to make, then ask for the Name, phone number, and email address for each person.

You will be writing this information to a file. Separate each value with a comma, and make sure to include the new line symbol.

Write this program using a function  - you should just need the main function
"""

def main():
    count = int(input("How many people do you want to add to this file?"))
    contacts = open('contacts.txt', 'w')
    for x in range (1, count + 1):
        name = input("What is the name of the person? ")
        phone = input("What is their phone number? ")
        email = input("What is their email address? ")
        contacts.write(name + ", " + phone + ", " + email + "\n")
main()
