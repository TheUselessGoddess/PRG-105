"""

Match strings in a list
Error Checking

"""


def main():
    accounts = open('accounts.txt', 'r')
    over90 = open('over90.txt', 'r')
    overarray = []
    matching = []
    line1 = over90.readline()
    line2 = accounts.readline()
    while line1 != '':
        overarray.append(line1.strip('\n'))
        line1 = over90.readline()
    while line2 != '':
        for x in overarray:
            if line2.find(x) != -1:
                matching.append(line2.strip('\n'))
        line2 = accounts.readline()
    print("The following accounts are overdue:\n")
    for x in matching:
        print(x)
main()

