'''Create a quiz based on learning the numbers from 1-10 in another language.'''



def main():
    print('Enter the number in English which corresponds to the French one.')
    numbers = ['un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix']
    numbers2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    score = 0
    count = 0
    for x in numbers:
        answer = input('What is the equivalent of ' + x + ': ')
        if answer.lower() == numbers2[count]:
            print('Correct')
            score += 1
        else:
            print('Incorrect. The answer was ' + numbers2[count])
        count += 1
    print('You got ' + str(score))
    if score >= 9:
        print('A')
    elif 7 < score < 9:
        print('B')
    elif 6 < score < 8:
        print('C')
    elif 5 < score < 7:
        print('D')
    else:
        print('F')
main()
