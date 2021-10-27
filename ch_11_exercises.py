"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)
# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:
    def __init__(self, number_of_rooms, square_feet, floors):
        self.Number_of_rooms = number_of_rooms
        self.Square_feet = square_feet
        self.Floors = floors

# 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_rooms(self, rooms):
        self.Number_of_rooms = rooms

    def set_feet(self, area):
        self.Square_feet = area

    def set_floors(self, floors):
        self.Floors = floors

# 3) Add accessors for all of the data attributes
    def get_rooms(self):
        return self.Number_of_rooms

    def get_area(self):
        return self.Square_feet

    def get_floors(self):
        return self.Floors

# 4) Create the class SingleFamilyHome as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes
class SingleFamilyHome(Dwelling):
    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)
        self.garage_type = garage_type
        self.yard_size = yard_size
# 5) Create the mutator and accessor methods for the garage_type and yard_size attributes
    def set_garage_type(self, garage_type):
        self.garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.yard_size = yard_size

    def get_yard_size(self):
        return self.yard_size

    def get_garage_type(self):
        return self.garage_type

# Demonstrate the SingleFamilyHome class, no need to import because you are in the same file
# 6) Create a main function.
# 7) In main, create an object from the Single_family_home class with the following information:
#            6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
def main():
    home = SingleFamilyHome('6', '1200', '1', 'Single Car Garage', '.25 Acres')
# 8) Display the data using the accessor methods
    print(home.get_rooms())
    print(home.get_area())
    print(home.get_floors())
    print(home.get_garage_type())
    print(home.get_yard_size())
# 9) Call the main function
main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)
# 1) Type in the mammal class from program 11-9, lines 1 - 22
# The Mammal class represents a generic mammal.

class Mammal:

      # The _ _init_ _ method accepts an argument for
      # the mammal's species.

      def __init__(self, species):
          self.species = species

      # The show_species method displays a message
      # indicating the mammal's species.

      def show_species(self):
          print('I am a', self.species)

      # The make_sound method is the mammal's
      # way of making a generic sound.

      def make_sound(self):
          print('Grrrrr')

# 2) Create a Mouse class as a sub class of the mammal class following the Dog example
class Mouse(Mammal):
    def __init__(self):
          Mammal.__init__(self, 'Mouse')
    def make_sound(self):
        print('Squeak')
# 3) Create an Sheep class as a sub class of the mammal class following the Cat Example
class Sheep(Mammal):
    def __init__(self):
          Mammal.__init__(self, 'Sheep')
    def make_sound(self):
        print('Baaaa')
# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Sheep class that you created
def main2():
    sheep = Sheep()
    mouse = Mouse()
    print('Here are some animals and the sounds they make.\n---------------------')
    show_mammal_info(mouse)
    show_mammal_info(sheep)

def show_mammal_info(creature):
      creature.show_species()
      creature.make_sound()

main2()
