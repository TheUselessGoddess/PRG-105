"""
    Variables provided-

    eligible_for_finanancial_aid = True # change value if any of the input makes the student ineligible

    User input (What information do you need to get from the user)

    student_status = # current or new

    gpa = # float

    criminal_record = # Boolean

credit_hours = # int

gross_yearly_income = # float

Processing:

student-status == new # keep going

student-status == current # ask gpa

GPA >= 2.0 # continue

else: eligible_for_financial_aid = False

criminal_drug_record - # if True eligible_for_financial_aid = False

credit_hours < 6 # eligible_for_financial_aid = False

    gross_yearly_income >= 50,000 #  eligible_for_finanacial_aid = False



    Output:

    either: Yes, you are eligible for financial aid or No, you are not eligible for financial aid.
"""
student_status = int(input("Are you a new student? Enter 1 for Yes and 2 for No"))
criminal_record = int(input("Do you have a criminal record? Enter 1 for Yes and 2 for No"))
yearly_income = float(input("What is your gross yearly income?"))
if student_status == 2:
    gpa = float(input("What is your GPA?"))
    credit_hours = int(input("How many credit hours do you have?"))
    if gpa >= 2.0 and credit_hours >= 6 and criminal_record == 2:
        print("You are eligible for financial aid.")
    else:
        print("You are not eligible for financial aid.")
elif student_status == 1:
    if criminal_record == 2 and yearly_income < 50000:
        print("You are eligible for financial aid.")
    else:
        print("You are not eligible for financial aid.")





