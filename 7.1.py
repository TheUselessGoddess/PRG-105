"""

Ask the user how many students are in their class. Get the student's name and final grade.
Store the answers in a two-dimensional list, then write the list to the grades.txt file.
outfile = open("grades.txt", "w")
for line in student_grades:
    lineout = "'" + line[0] + "', '" + line[1] + "'\n"
    outfile.writelines(lineout)
outfile.close()
"""

def creation():
    count = int(input("How many students do you need to enter grades for?"))
    outfile = open("grades.txt", "w")
    list = []
    for x in range(1, count + 1):
        name = input("Enter the name of student " + str(x) + ": ")
        grade = input("Enter the student's final letter grade.")
        list.append([name, grade])
    for line in list:
        lineout = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineout)
        outfile.close()
    outfile = open("grades.txt", 'r')
    for line in outfile:
        print(str(line))
creation()
