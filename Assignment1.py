peak_connection= 0.6
offpeak_connection= 0.3

peak_per_unit = 0.4
offpeak_per_unit = 0.2

tariff = int(input('Choose one \n 1.Peak \n 2.OffPeak \n answer: '))

if tariff >3:
    print("bad input")

calltimeM = int(input('Minutes: '))
calltimeS = int(input('Seconds: '))

#In case of input over 60 seconds
if calltimeS > 60:
    print('bad input')
#Get a unit 
elif calltimeS%30 >= 15:
    unit = calltimeM/2 + calltimeS//30 +1
else:
    unit = calltimeM/2 + calltimeS//30

#peaktime call charge
if tariff == 1:
    total_charge = peak_connection + unit*peak_per_unit
    print('Total charge : $', format(total_charge, '.2f'))
#Offpeaktime call charge
else:
    total_charge = offpeak_connection + unit*offpeak_per_unit
    print('Total charge : $', format(total_charge,'.2f'))








