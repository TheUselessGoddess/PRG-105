import furniture
import desk
#Complaining about it but it still works
def main():
    parent = furniture.Office_Furniture('Desk', 'Metal', '10cm', '40cm', '20cm', '$20')
    child = desk.Desk('Desk', 'Metal', '10cm', '40cm', '20cm', '$20', 'Left', '3')
    print(parent)
    print(child)
main()
