
# 1. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

arr = []

with open('dataset/nyc_weather.csv') as file:
    for line in file:
        each_line = line.split(',')
        try:
            temp = int(each_line[1])
            arr.append(temp)
        except:
            print('Invalid, so ignoring !!')


# What was the average temperature in first week of Jan

print("The average temperature in first week of Jan is: ", sum(arr[:7])/len(arr[:7]))

# What was the maximum temperature in first 10 days of Jan
print("The average temperature in first week of Jan is: ", max(arr[:10]))


# 2. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

weather_dict = {}

with open('dataset/nyc_weather.csv') as file:
    for line in file:
        each_line = line.split(',')
        try:
            val = int(each_line[1])
            key = str(each_line[0])
            weather_dict[key] = val
        except:
            print('Invalid, so ignoring !!')

# What was the temperature on Jan 9?
print(weather_dict['09-Jan'])


# What was the temperature on Jan 4?
print(weather_dict['04-Jan'])  