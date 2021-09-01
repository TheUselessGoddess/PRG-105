"""
You are writing a program to sell tickets to the school play. If the person buying the tickets is a student, their price is $5.00 per ticket. If the person buying the tickets is a veteran, their price is $7.00 per ticket. If the person buying the ticket is a sponsor of the play, the price is $2.00 per ticket. If the person buying the ticket is a part of the general public, the price is $10.00.

Prices by who is purchasing the tickets:

student: $5.00

Veteran: $7.00

Show Sponsor: $2.00

Retiree: $6.00

General public: $10.00



People buying 4 - 8 tickets get a 10% discount.

People buying 9-15 tickets get a 15% discount.

People buying more than 15 tickets get a 20% discount.



Determine who is buying the tickets, how many tickets they want, and display their total cost and cost per ticket after the discount is applied—format as money.

Sample:

PLAY PRICES PER TICKET
1. Student $5.00
2. Veteran $7.00
3. Show Sponsor $2.00
4. Retiree $6.00
5. General Public $10.00


Please enter the number of the category you fit for purchasing tickets: 4
How many tickets would you like to buy? 20


Cost before any discounts were applied: $120.00
Your price after all discounts were applied is 96.00
Your price is $4.80 per ticket.
"""
ticket_count = int(input("How many tickets do you plan to buy?"))
print("1. Student $5.00\n2. Veteran $7.00\n3. Show Sponsor $2.00\n4. Retiree $6.00\n5. General Public $10.00")
group = int(input("Enter the number of the group you fall under."))
if group == 1:
    if ticket_count > 15:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 5.00, '.2f')))
        print("Cost after discounts were applied: $" + str((format(ticket_count * 5.00) * 0.8, '.2f')))
        print("Your price per ticket is: $" + str(format(5.00 * 0.8, '.2f')))
    elif ticket_count > 8:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 5.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 5.00) * 0.85, '.2f')))
        print("Your price per ticket is: $" + str(format(5.00 * 0.85, '.2f')))
    elif ticket_count > 3:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 5.00, '.2f')))
        print("Cost after discounts were applied: $" + str((format(ticket_count * 5.00) * 0.9, '.2f')))
        print("Your price per ticket is: $" + str(format(5.00 * 0.9, '.2f')))
    else:
        print("Cost for your tickets is: $" + str(format(ticket_count * 5.00, '.2f')))
elif group == 2:
    if ticket_count > 15:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 7.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 7.00) * 0.8, '.2f')))
        print("Your price per ticket is: $" + str(format(7.00 * 0.8, '.2f')))
    elif ticket_count > 8:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 7.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 7.00) * 0.85, '.2f')))
        print("Your price per ticket is: $" + str(format((ticket_count * 7.00) * 0.85, '.2f')))
    elif ticket_count > 3:
        print("Cost before any discounts were applied: $" + str(ticket_count * 7.00))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 7.00) * 0.9, '.2f')))
        print("Your price per ticket is: $" + str(format(7.00 * 0.9, '.2f')))
    else:
        print("Cost for your tickets is: $" + str(format(ticket_count * 7.00, '.2f')))
elif group == 3:
    if ticket_count > 15:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 2.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 2.00) * 0.8, '.2f')))
        print("Your price per ticket is: $" + str(format(2.00 * 0.8, '.2f')))
    elif ticket_count > 8:
        print("Cost before any discounts were applied: $" + str(ticket_count * 2.00))
        print("Cost after discounts were applied: $" + str(float(ticket_count * 2.00) * 0.85))
        print("Your price per ticket is: $" + str(format(2.00 * 0.85, '.2f')))
    elif ticket_count > 3:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 2.00)))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 2.00) * 0.9, '.2f')))
        print("Your price per ticket is: $" + str(format(2.00 * 0.9, '.2f')))
    else:
        print("Cost for your tickets is: $" + str(ticket_count * 2.00))
elif group == 4:
    if ticket_count > 15:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 6.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 6.00) * 0.8, '.2f')))
        print("Your price per ticket is: $" + str(format(6.00 * 0.8, '.2f')))
    elif ticket_count > 8:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 6.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 6.00) * 0.85, '.2f')))
        print("Your price per ticket is: $" + str(format(6.00 * 0.85, '.2f')))
    elif ticket_count > 3:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 6.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 6.00) * 0.9, '.2f')))
        print("Your price per ticket is: $" + str(format(6.00 * 0.9, '.2f')))
    else:
        print("Cost for your tickets is: $" + str(format(ticket_count * 6.00, '.2f')))
elif group == 5:
    if ticket_count > 15:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 10.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 10.00) * 0.8, '.2f')))
        print("Your price per ticket is: $" + str(format(10.00 * 0.8, '.2f')))
    elif ticket_count > 8:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 10.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 10.00) * 0.85, '.2f')))
        print("Your price per ticket is: $" + str(format(10.00 * 0.85, '.2f')))
    elif ticket_count > 3:
        print("Cost before any discounts were applied: $" + str(format(ticket_count * 10.00, '.2f')))
        print("Cost after discounts were applied: $" + str(format((ticket_count * 10.00) * 0.9, '.2f')))
        print("Your price per ticket is: $" + str(format(10.00 * 0.9, '.2f')))
    else:
        print("Cost for your tickets is: $" + str(ticket_count * 10.00))
