import os
import json
import calendar

def read_data(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as file:
        content = json.load(file)
        return content


def write_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def max_temperature(data):
    if not data:
        return None
    return max(data, key=lambda date: data[date]['t'])


def min_temperature(data):
    if not data:
        return None
    return min(data, key=lambda date: data[date]['t'])


def max_humidity(data):
    if not data:
        return None
    return max(data, key=lambda date: data[date]['h'])


def min_humidity(data):
    if not data:
        return None
    return min(data, key=lambda date: data[date]['h'])


def tot_rain(data, date):
    total = 0.0
    for key, stored in data.items():
        if date in key:
            total += stored["r"]
    return total


def heading():
    return f'{"Date":25} {"Time":13} {"Temperature":18} {"Humidity":10} {"Rain":>10}'


def report(data, key):
    if key not in data:
        return "Error"

    year = key[0:4]
    month = int(key[4:6])
    day = key[6:8]
    hours = key[8:10]
    minutes = key[10:12]
    seconds = key[12:14]

    month_name = calendar.month_name[month]

    stored_data = data[key]
    temp = stored_data['t']
    humidity = stored_data['h']
    rain = stored_data['r']

    date_str = f"{month_name} {day}, {year}"
    time_str = f"{hours}:{minutes}:{seconds}"

    return f"{date_str:25} {time_str:13} {temp:18} {humidity:10} {rain:>10}"


def report_historical(data):

    if not data:
        return "No data available."


    max_temp_key = max_temperature(data)
    min_temp_key = min_temperature(data)

    max_hum_key = max_humidity(data)
    min_hum_key = min_humidity(data)

    return (
        f"{heading()}\n"
        f"{report(data, max_temp_key)} (Highest Temperature)\n"
        f"{report(data, min_temp_key)} (Lowest Temperature)\n"
        f"{report(data, max_hum_key)} (Highest Humidity)\n"
        f"{report(data, min_hum_key)} (Lowest Humidity)\n"
    )
