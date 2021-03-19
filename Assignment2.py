#Programming1 GYUHUN SIM 

#Price table
stall_wd = 75
stall_we = 105
stall_cs = 55

dressCircle_wd = 85
dressCircle_we = 115
dressCircle_cs = 65

upperCircle_wd = 60
uppercircle_we = 85
uppercircle_cs = 40

#Function changing number to day
def weekday(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    else:
        return "Sunday"

#Final ticket cost statement
def cost_cal(num1):
    print('\nFinal ticket cost: $',format(num1,',.2f'), '\n')

#To start while loop
keep_going = 'Y'

while keep_going == 'Y' or keep_going == 'y':
    print('++++++++++++++++++++++++++++++++++++++++++++++')
    print('WELCOME TO TICKETPLACE BOOKINGS')

#Ticket value error check
    while True:
        try:
            ticket = int(input('Number of tickets required: '))
            break
        except ValueError:
            print ("Please Enter number again...")

#Select seat area       
    seatArea = input('Seating Area((S)talls, (D)ress circle, (U)pper circle): ')

#
    while True:
        day = input('Day of the week(1-->7=Monday-->Sunday: ')
        try:
            day = int(day)
        except ValueError:
            print("Please enter number again...")
            continue
        if day > 7 or day < 0 :
            print("Please enter valid number")
            continue
        else:
            break

#Choose Y or N membership
    member = input('Member(Y/N): ')
    
#Concession number error check
    while True:
        concession = input('Number of concession tickets included(under 18, over 65 or student): ')
        try:
            concession = int(concession)
        except ValueError:
            print("Please enter number again...")
            continue

        if ticket < int(concession):
            print("The number of concession can't be higher than the number of tickets")
            continue
        else:
            break
        
        

#Show seat area that user's choice
    print('--You are purchasing',ticket,'tickets for', weekday(day), '--', end =' ')
    if seatArea == "S":
        print('You are sitting in the Stalls--')
    elif seatArea == "D":
        print('You are sitting in the Dress Circles--')
    else:
        print('You are sitting in the Upper Circles--')

#Member and bulk discount
    print('--',concession,'Concessions chosen--',end="")
    if member == 'Y' or member == 'y':
        print('Memeber Discount Applied --',end="")
    
    if ticket >= 6:
        print('Bulk Discount Applied--')

#cost calculation SA = Seating Area 
    ticket_adult = ticket - concession
    if seatArea == 'S':
        if day>=1 and day<=5:
            cost = ticket_adult * stall_wd + concession * stall_cs
        else:
            cost = ticket * stall_we
    elif seatArea == 'D':
        if day>=1 and day<=5:
                cost = ticket_adult * dressCircle_wd + concession * dressCircle_cs
        else:
            cost = ticket * dressCircle_we
    else:
        if day>=1 and day<=5:
                cost = ticket_adult * upperCircle_wd + concession * uppercircle_cs
        else:
            cost = ticket * uppercircle_we

#Member or bulk discount applying
    if member == 'Y' and ticket >= 6:
        cost = cost*0.9 *0.95
        cost_cal(cost)
        
    elif member == 'Y' and ticket < 6:
        cost = cost*0.9
        cost_cal(cost)

    elif member !='Y' and ticket >= 6:
        cost = cost*0.95
        cost_cal(cost)
    else:
        cost_cal(cost)

    keep_going = input('Book another ticket? (Y)es or (N)o: ')

print('++++++++++++++++++++++++++++++++++++++++++++++')