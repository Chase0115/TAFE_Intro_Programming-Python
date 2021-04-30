def max_index(list_name):
    maximum = max(list_name)
    maximum_index = list_name.index(maximum)
    return maximum_index


def min_index(list_name):
    minimum = min(list_name)
    minimum_index = list_name.index(minimum)
    return minimum_index


def average_volume(list_name):
    average = sum(list_name) / len(list_name)
    return average

# read 'AAPL_Volume' + exception
def read_file():
    file_name = 'AAPL_Volume.txt'
    try:
        infile = open(file_name, 'r')
        return infile
    except IOError:
        print(f"Cannot load the file {file_name}")


apple_stock_file = read_file()

# split in two list
apple_date = []
apple_volume = []
while True:
    line = apple_stock_file.readline()
    if line == '':
        break
    date = line[:10].strip()
    apple_date.append(date)
    volume = int(line[11:].strip())
    apple_volume.append(volume)

# close the file
apple_stock_file.close()

# Count February and March trading day
feb_days_count = 0
mar_days_count = 0
for date in apple_date:
    month = date[-7:-5]
    if month == '02':
        feb_days_count += 1
    elif month == '03':
        mar_days_count += 1

# Define Maximum and minimum volume
minimum = min_index(apple_volume)
maximum = max_index(apple_volume)

# Calculate Average volume
feb_average = format(average_volume(apple_volume[:feb_days_count]), '.2f')
mar_average = format(average_volume(apple_volume[feb_days_count:mar_days_count]), '.2f')

# Define Higher volume
feb_total_volume = sum(apple_volume[:feb_days_count])
mar_total_volume = sum(apple_volume[feb_days_count:mar_days_count])
if feb_total_volume > mar_total_volume:
    higher_volume = 'February'
else:
    higher_volume = 'March'

# Output
print(f"{apple_date[maximum]} has the maximum trade volume of {apple_volume[maximum]}")
print(f"{apple_date[minimum]} has the maximum trade volume of {apple_volume[minimum]}")
print(f"The average trade volume of February is {feb_average}")
print(f"The average trade volume of March is {mar_average}")
print(f"AAPL has higher trading volume in {higher_volume} ")
