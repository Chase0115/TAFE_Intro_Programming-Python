# information
# p = initial number of GPs(read from data.txt)
# d= number of days being calculated
# v= vaccination rate
# gc = growth rate of vaccination centers
# gv = growth rate of accredited GPs for vaccination
# r = vaccine refusal rate
# v = v x (1 + (10gc+gv-r)/100)
# -> vaccination number = p * v * d

# Todo: import math,time module
import time
from pandas import DataFrame as df


# Todo: function v = v x (1 + (10gc+gv-r)/100)
def cal_vacc_rate(v, gc, gv, r):
    """v = init_vacc_rate
        gc = growth_rate_vacc_center
        gv = growth_rate_GPs
        r = refusal_rate"""
    vacc_rate = v * (1 + (10 * gc + gv - r) / 100)
    return vacc_rate


# Todo: function vaccination number = p * v * d
def cal_vacc_number(p, v, d):
    """p = initial number of GPs
        v = vaccination rate
        d = number of days being calculated"""
    vacc_number = p * v * d
    return vacc_number


def list_of_num_vacc(num_of_gp, v, d):
    state_vacc_number = []
    for state in num_of_gp:
        p = num_of_gp[state]
        vacc_number = round(cal_vacc_number(p, v, d))
        state_vacc_number.append(vacc_number)
    total = sum(state_vacc_number)
    state_vacc_number.append(total)
    return state_vacc_number


# Todo: calculate required days for complete vaccination of each State and Whole Australia
population = {'NSW': 6000000, 'ACT': 300000, 'QLD': 4500000, 'VIC': 4500000, 'SA': 1000000, 'WA': 2000000,
              'TAS': 400000, 'NT': 200000}


def complete_vaccination(population, vacc_number):
    total_state_population = []
    total_population = 0
    for state in population:
        total_state_population.append(population[state])
        total_population += population[state]
    total_state_population.append(total_population)


# Todo: read data from data.txt.
gpfile = open('data.txt', 'r')
lines = gpfile.readlines()
gpfile.close()

# Todo: make dictionary the number of GPs
gpfile = open('data.txt', 'r')
num_of_gp = {}
for line in range(1, len(lines), 2):
    state = gpfile.readline().strip()
    gp_number = int(gpfile.readline().strip())
    num_of_gp[state] = gp_number
gpfile.close()


def report_process():
    # Todo: take user input(vaccination_rate,growth_rate_center,growth_rate_GPs,refusal_rate,given_days)
    init_vacc_rate = int(input("Enter the rate of vaccination : "))
    growth_rate_center = int(input("Enter the growth rate of vaccination centres : "))
    growth_rate_gp = int(input("Enter the growth rate of accredited GPs for vaccinating : "))
    refusal_rate = int(input("Enter the vaccine refusal rate due to possible side effects : "))
    given_day = int(input("Enter the number of days to calculate into the future : "))

    v = cal_vacc_rate(init_vacc_rate, growth_rate_center, growth_rate_gp, refusal_rate)

    # Todo: make a list and put in the list of vaccinated people's number
    vaccinated_people = []
    day = 0
    while day < given_day:
        vaccinated_people.append(list_of_num_vacc(num_of_gp, v, day + 1))
        day += 1

    # Todo: print output
    print(f"COVID-19 VACCINATION NUMBERS - {given_day}DAY PREDICTIONS")
    print(f"VACCINATION RATE: {init_vacc_rate}")
    print(f"CENTRE GROWTH: {growth_rate_center}%")
    print(f"ACCREDITED GP GROWTH: {growth_rate_gp}%")
    print(f"REFUSAL RATE: {refusal_rate}%")

    # Todo: print table
    col = ["NSW", "ACT", "QLD", "VIC", "SA", "WA", "TAS", "NT", "Total"]
    ind = []
    for i in range(given_day):
        ind.append(f"day{i + 1}")
    table = df(data=vaccinated_people, columns=col, index=ind)

    # Todo: display result
    str_table = table.to_string()
    print(str_table)

    # Todo: each time extract file (name: report_s.txt) use time.time() function
    s = int(time.time())
    file_report = open(f"report_{s}.txt", "w")
    file_report.write(str_table)
    file_report.close()


# Todo: loop the running function
make_report = True
while make_report:
    report_process()
    keep_going = input("Do you want to make another report? [Y/N] : ").lower()
    if keep_going == 'y':
        make_report = True
    else:
        make_report = False
