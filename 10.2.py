'''
n this programming exercise, you will create a simple trivia game for two players. The program will work like this:

Starting with player 1, each player gets a turn at answering 5 trivia questions. (There should be a total of 10 questions.)
When a question is displayed, 4 possible answers are also displayed. Only one of the answers is correct, and if the player selects the correct answer,
 he or she earns a point.
After answers have been selected for all the questions, the program displays the number of points earned by each player and declares the player
 with the highest number of points the winner.
To create this program, write a Question class to hold the data for the trivia question. The question class should have attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question Objects, one for each trivia question.
Make up your own trivia question on the subject or subjects of your choice for the objects.
'1. Who was elected President of the United States in 2017?': ['', '', '', ''],
'''

class Trivia_game:
    def __init__(self):
        self.questions = {'1. Who was elected President of the United States in 2017?': ['Trump', 'Biden', 'Obama', 'Washington'],
                          '2. When did Jonas Brothers make their comeback to the music world?': ['2015', '2011', '2019', '2014'],
                          '3. What is the national language of Canada?': ['English', 'Dutch', 'French', 'Spanish'],
                          '4. What is the national animal of Pakistan?': ['Peacock', 'Markhor', 'Loin', 'Lion'],
                          '5. A la Crecy is a French dish made of what?': ['Apples', 'Carrots', 'Potatos', 'Yams'],
                          '6. What native country is Brazil?': ['South American', 'North American', 'West American', 'Central American'],
                          '7. Which core ingredient is important to cook a savory dish?': ['Salt', 'Butter', 'Sugar', 'Brown Sugar'],
                          '8. Brazil is the biggest producer of?': ['Rice', 'Oil', 'Coffee', 'Sugar'],
                          '9. Saudi Arabia is the biggest producer of?': ['Oil', 'Coal', 'Coffee', 'Paper'],
                          '10. Which country is infamously known as Arch Rival of Pakistan?': ['Afghanistan', 'America', 'India', 'Russia']}
        self.correct_answer = [0, 2, 1, 1, 1, 1, 0, 2, 0, 2]
        self.player_one_score = 0
        self.player_two_score = 0
        self.active_player = 'Player One'

    def check_answer(self, choice, question):
        if (int(choice) - 1) == self.correct_answer[question]:
            if self.active_player == 'Player One':
                self.player_one_score += 1
            else:
                self.player_two_score += 1

    def output_questions(self):
        count = 0
        for x in self.questions:
            if count % 2 == 0:
                self.active_player = 'Player One'
            else:
                self.active_player = 'Player Two'
            print(x)
            for y in range(0, 4):
                print('\t' + str(y + 1) + '. ' + self.questions[x][y])
            answer = input()
            self.check_answer(answer, count)
            count += 1
        self.get_score()

    def get_score(self):
        print("Player One's Score is: " + str(self.player_one_score) + '\n' + "Player Two's Score is: " + str(self.player_two_score))
        if self.player_one_score > self.player_two_score:
            print('The winner is Player One')
        elif self.player_one_score < self.player_two_score:
            print('The winner is Player Two')
        elif self.player_one_score == self.player_two_score:
            print('There is no winner. It is a Tie')

def main():
    print('To answer a question enter the corresponding number of your choice.')
    trivia = Trivia_game()
    trivia.output_questions()
main()
