"""
Use the program from 6.2 as a start
 Open the sales_error-1.txt   Download sales_error-1.txt file as the infile
One of the numbers has an error - use the try and except statement to make it ignore the line with the error, report it to the screen
Also detect if there is a bad file name, test that by looking for bad filename

"""


def main():
    file = 'sales_error.txt'
    try:
        sales = open(file, 'r')
        count = 0
        line = sales.readline()
        value = 0.0
        while line != '':
            try:
                count += 1
                print(format(float(line.strip('\n')), ',.2f'))
                value += float(line.strip('\n'))
                line = sales.readline()
            except ValueError:
                count += 1
                print("Line " + str(count) + " with a value of " + line.strip('\n') + " was invalid")
                line = sales.readline()
        print("Total: " + str(format(value, ',.2f')) + "\n" + "Number of entries: " + str(count) + "\n" + "Average: " + str(format((value / count), ',.2f')))
    except FileNotFoundError:
        print(file + " does not exist.")
main()

