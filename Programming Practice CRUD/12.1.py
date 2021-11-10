import pickle

def main():
    repeat = 0
    try:
        file = open('customer_file.dat', 'rb')
        pb = pickle.load(file)
        data = pb
    except:
        data = {}
    while repeat != 5:
            repeat = 0
            try:
                repeat = int(input('What would you like to do?\n1. Add New Record\n2. View Records\n3. Change a Record\n4. Remove a Record\n5. Quit '))
            except ValueError:
                print('--That was not a valid entry. Please enter a valid entry.--')
                continue
            if repeat == 5:
                print('Goodbye')
                break
            elif repeat == 1:
                create(data)
            elif repeat == 2:
                view(data, 1)
            elif repeat == 3:
               change(data)
            elif repeat == 4:
                remove(data)

def change(data):
    view(data, 2)
    value = int(input("What would you like to change?\t1. Name 2. Email 3. Both "))
    if value == 1:
        name = input('Please enter the current name for the entry you wish to modify.')
        data[input('Enter the new name for the chosen entry. ')] = data.pop(name)
    elif value == 2:
        data[input('Please enter the name of the person whose email you are changing. ')] = input('Please enter the new email for the chosen entry. ')
    elif value == 3:
        name = input('Please enter the current name for the data pair you wish to modify. ')
        data[name] = input('Please enter the new email for the chosen entry. ')
        data[input('Enter the new name for the chosen entry. ')] = data.pop(name)
    save(data)

def remove(data):
    view(data, 2)
    choice = input('Who would you like to remove? ')
    if choice in data.keys():
        if int(input('You would like to remove ' + choice + '?\t 1. Yes 2. No ')) == 1:
            del data[choice]
    else:
        print('That entry does not exist.')
    save(data)

def view(data, repeat2):
    again = 1
    line = ''
    if int(input('Would you like a line of space between each entry?\t1. Yes 2. No ')) == 1:
        line = '\n'
    while again != 2:
        person = input('Who would you like to look for? If you would like to see all data please enter "All" ')
        if person in data.keys() and person.lower() != 'all':
            print('Name: ' + person + ', Email: ' + data[person])
        elif person.lower() == 'all':
            if data:
                for x in data:
                    print()
                    print('Name: ' + x + ', Email: ' + data[x] + line)
            else:
                print('There are no people/emails yet.')
        elif person.lower() != 'all':
            print('Does not exist.')
        if repeat2 == 1:
            again = int(input("Would you like to view another person's data?\t1. Yes 2. No "))
            if again == 2:
                break
        elif repeat2 == 2:
            break

def create(data):
    person = input('What is the name of the person you are adding? ')
    data[person] = input('What is the email of the person you are adding? ')
    print('Thank you, customer ' + person + ' has been added ')
    save(data)

def save(data):
    output_file = open('customer_file.dat', 'wb')
    pickle.dump(data, output_file)
    output_file.close()
    print('\n---The file has been updated and saved---\n')

main()
