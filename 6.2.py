"""
Open the file sales_totals in read mode (Download: sales_totals.txt   Download sales_totals.txt )
Read in all the lines using a loop
Strip the newline symbol and convert each line to a float
Add each number to the running total
Count the number of lines
Format and display each number
Outside of the loop format and display the total, the count, and the average
Do this in functions

line = line.strip('\n')
"""


def main():
    sales = open('sales_totals.txt', 'r')
    count = 0
    value = 0.0
    line = sales.readline()
    value = 0.0
    while line != '':
        count += 1
        print(format(float(line.strip('\n')), ',.2f'))
        value += float(line.strip('\n'))
        line = sales.readline()
    print("Total: " + str(format(value, ',.2f')) + "\n" + "Number of entries: " + str(count) + "\n" + "Average: " + str(format((value / count), ',.2f')))
main()

