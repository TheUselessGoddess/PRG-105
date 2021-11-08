class Office_Furniture:
    def __init__(self, category, material, length, width, height, price):
        self.category = category
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = price

    def __str__(self):
        return str(self.category) + ' ' + str(self.material) + ' ' + str(self.length) + ' ' + str(self.width) + ' ' + str(self.height) + ' ' + str(self.price)

    def set_category(self, category):
        self.category = category

    def set_material(self, material):
        self.material = material

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_price(self, price):
        self.price = price
    #simple function to set all the values at once
    def set_all(self, category, material, length, width, height, price):
        if category != '':
            self.category = category
        if material != '':
            self.material = material
        if length != '':
            self.length = length
        if width != '':
            self.width = width
        if height != '':
            self.height = height
        if price != '':
            self.price = price


