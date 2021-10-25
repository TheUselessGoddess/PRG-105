'''
Write Classes
Work with class diagrams
Write get and set methods
Create instances of a class
'''

class Person_data:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.age = 0
        self.phone = ''
    def set_name(self, chosen_name):
        self.name = chosen_name
    def set_address(self, chosen_address):
        self.address = chosen_address
    def set_age(self, chosen_age):
        self.age = chosen_age
    def set_phone(self, chosen_phone):
        self.phone = chosen_phone
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_age(self):
        return str(self.age)
    def get_phone(self):
        if self.phone != '':
            return self.phone
        else:
            return 'N/a'

my_info = Person_data()
mother_info = Person_data()
father_info = Person_data()

def addinfo():
    my_info.set_name('Nick')
    my_info.set_address("Home")
    my_info.set_age(19)
    my_info.set_phone('111-111-1111')

    mother_info.set_name('Kristi')
    mother_info.set_address('Home')
    mother_info.set_age(45)
    mother_info.set_phone('222-222-2222')

    father_info.set_name('Randy')
    father_info.set_address('Home 2')
    father_info.set_age(52)
    father_info.set_phone('333-333-3333')

def main():
    addinfo()
    print('Name is ' + my_info.get_name())
    print('Address is ' + my_info.get_address())
    print('Age is ' + my_info.get_age())
    print('Phone number is ' + my_info.get_phone() + '\n')

    print('Name is ' + mother_info.get_name())
    print('Address is ' + mother_info.get_address())
    print('Age is ' + mother_info.get_age())
    print('Phone number is ' + mother_info.get_phone() + '\n')

    print('Name is ' + father_info.get_name())
    print('Address is ' + father_info.get_address())
    print('Age is ' + father_info.get_age())
    print('Phone number is ' + father_info.get_phone())

main()
