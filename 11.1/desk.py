
import furniture
#Complaining about it but it still works


class Desk(furniture.Office_Furniture):

    def __init__(self, category, material, length, width, height, price, location_of_drawers, number_of_drawers):
        furniture.Office_Furniture.__init__(self, category, material, length, width, height, price)
        self.location_of_drawers = location_of_drawers
        self.number_of_drawers = number_of_drawers

    def __str__(self):
        furniture.Office_Furniture.__str__(self)
        return str(self.category) + ' ' + str(self.material) + ' ' + str(self.length) + ' ' + str(self.width) + ' ' + str(self.height) + ' ' + str(self.price) + ' ' + str(self.location_of_drawers) + ' ' + str(self.number_of_drawers)

    def set_location(self, location):
        self.location_of_drawers = location

    def set_number(self, number):
        self.number_of_drawers = number
