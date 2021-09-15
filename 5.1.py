"""
Create a program that presents the user with five choices. The topic could be game characters, food, car packages, anything you are interested in.
 You will put a menu on the screen, ask the user to enter the number or letter of their choice,
 and then call the corresponding function to give the user more information.
"""
choice = int(input("What topic would you like to know more about?\n1. Percy Jackson Series\n2. Ham and cheese sandwich\n3. Minecraft\n4. Electroblob's Wizardry\n5. Fallout 4"))


def percyJackson():
    print("The 5 books of the percy jackson series are:\n1. The Lightning Thief\n2. The Sea of Monsters\n3. The Titan's Curse\n4. The Battle of the Labryinth\n5. The Last Olympian")
def sandwich():
    print("The typical components of a Ham and cheese sandwich are: Ham, some type of cheese, and bread.")
def minecraft():
    print("Minecraft is a 3D 'Block based' game that was made in 2009.")
def wizardry():
    print("Electroblob's Wizardry is a magic mod that was made for minecraft using the 'Forge' program")
def fallout():
    print("Fallout 4 is a post-apocalyptic survival and story game made by Bethesda.")
if choice == 1:
    percyJackson()
elif choice == 2:
    sandwich()
elif choice == 3:
    minecraft()
elif choice == 4:
    wizardry()
elif choice == 5:
    fallout()
