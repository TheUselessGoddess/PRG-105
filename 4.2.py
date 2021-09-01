"""
Use loops to make all the lyrics of "99 bottles of beer on the wall"  print on the screen. Adjust the last two verses for correct grammar:
"""
num = 99
while num > 0:
    if num == 1:
        print(str(num) + " bottle of beer on the wall,")
        print(str(num) + " bottle of beer")
        print("Take one down, pass it around")
        num -= 1
        print(str(num) + " bottles of beer on the wall\n")
    elif num == 2:
        print(str(num) + " bottles of beer on the wall,")
        print(str(num) + " bottles of beer")
        print("Take one down, pass it around")
        num -= 1
        print(str(num) + " bottle of beer on the wall\n")
    else:
        print(str(num) + " bottles of beer on the wall,")
        print(str(num) + " bottles of beer")
        print("Take one down, pass it around")
        num -= 1
        print(str(num) + " bottles of beer on the wall\n")

