"""
Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit.
"""
credit_score = int(input('What is your credit score?'))
if 300 <= credit_score <= 629:
    print("With a credit score of " + str(credit_score) + ". You have bad credit.")
elif 630 <= credit_score <= 689:
    print("With a credit score of " + str(credit_score) + ". You have fair credit.")
elif 690 <= credit_score <= 719:
    print("With a credit score of " + str(credit_score) + ". You have good credit.")
elif 720 <= credit_score <= 820:
    print("With a credit score of " + str(credit_score) + ". You have excellent credit.")
