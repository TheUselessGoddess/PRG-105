"""
Create dictionaries
Use for loops with dictionaries

data = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednseday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
format(, ',d')
"""

def main():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
    sum = 0
    count = 0
    high = []
    low = []
    highest = 0
    lowest = 0
    print('You will be entering the date and the number of steps taken for each day in a week.')
    for x in week:
        value = int(input('Please enter the number of steps you took on ' + x + ': '))
        data[x] = value
    highest = max(data.values())
    lowest = min(data.values())
    for x in data:
        sum += data[x]
        if data[x] == highest:
            high.append(count)
        elif data[x] == lowest:
            low.append(count)
        count += 1
    print('You walked a total of ' + str(format(sum, ',')) + ' steps during the week.\nThat was an average of ' + str(format(sum / 7, ',.0f')))
    print('The maximum amount of steps you took were: ' + str(format(highest, ',')) + ' on')
    for x in high:
        print('\t' + week[x])
    print('The minimum amount of steps you took were: ' + str(format(lowest, ',')) + ' on')
    for x in low:
        print('\t' + week[x])
main()
