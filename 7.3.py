"""
Ask the user for the name of the file to import (this should be the file you created in the last program)
Use try and except statements to ensure the file is there
read the file into python
Step through the list (strip the \n!)
Convert the coded message to English and display the message on the screen
"""
def main():
    filename = 'code.txt'
    normal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '?', '.', ',']
    code = [' ', '.', '?', '!', ',', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B']
    try:
        file = open(filename, 'r')
        changed = ""
        for letter in file:
            for item in range(0, len(code)):
                if letter.strip('\n').upper() == code[item]:
                    changed += normal[item]
        print(changed)
    except FileNotFoundError:
        print("File Not found")
main()
