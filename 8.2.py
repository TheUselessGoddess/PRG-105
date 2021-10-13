"""
Import a file into a list
Break apart list items into individual components by splitting strings
Split strings on a symbol
Check to see if data is numeric
"""
def main():
    rain = open('rainfall-totals-1.txt', 'r')
    values = []
    line = rain.readline()
    alldigit = False
    values.extend(line.split())
    while line != '':
        line = rain.readline()
        values.extend(line.split())
    for x in range(1, len(values), 2):
        tester = values[x].replace('.', '')
        if True == tester.isnumeric():
            alldigit = True
        else:
            alldigit = False
    print(alldigit)
main()
