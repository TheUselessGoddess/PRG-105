"""
Using parallel arrays, create a secret code creator.
Ask the user for text to enter, convert it to the code and write the code to a text file. Include punctuation (. , !), space, upper, and lower case letters.
"""

def main():
    normal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '?', '.', ',']
    code = [' ', '.', '?', '!', ',', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B']
    file = open('code.txt', 'w')
    phrase = input("Please enter a phrase to be translated into a secret phrase.")
    changed = ""
    for letter in phrase:
        for item in range(0, len(normal)):
            if letter.upper() == normal[item]:
                changed += code[item] + "\n"
                file.write(code[item] + '\n')

    print(changed)
main()
