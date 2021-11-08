class Employee:
    def __init__(self, name, number):
        self.employee_name = name
        self.number = number

    def get_name(self):
        return self.employee_name

    def get_number(self):
        return self.number

    def set_name(self, name):
        self.employee_name = name

    def set_number(self, number):
        self.number = number

class ProductionWorker(Employee):
    def __init__(self, name, pay, number, shift):
        Employee.__init__(self, name, number)
        self.pay = pay
        if shift == 1:
            self.shift = 'Day'
        else:
            self.shift = 'Night'

    def set_pay(self, pay):
        self.pay = pay

    def set_shift(self, shift):
        self.shift = shift

    def get_pay(self):
        return self.pay

    def get_shift(self):
        return self.shift


