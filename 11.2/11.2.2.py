import employee

def main():
    access = employee.ProductionWorker(input('Enter Employee Name: '), input('Enter employee number: '), input('Enter pay rate: '), input('Enter shift number: '))
    print(access.get_name())
    print(access.get_number())
    print(access.get_pay())
    print(access.get_shift())
main()
