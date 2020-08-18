import requests
import re
from datetime import datetime as dt
from matplotlib import pyplot

# (\d{2}-[A-Z]{3}-\d{4})\s+(\d+)

def get_rain_files(url):
    response = requests.get(url)
    data = response.text
    
    rain_files = re.findall(r"\w+\.rain", data)
    return rain_files

def get_rain_data(url, rain_file):
    response = requests.get(url+rain_file)
    data = response.text
    rain_data = re.findall(r"(\d{2}-[A-Z]{3}-\d{4})\s+(\d+)", data)
    return rain_data

def format_data(data):
    annual = {}
    for day in data:
        date = dt.strptime(day[0], '%d-%b-%Y')
        if date.year not in annual:
            annual[date.year] = int(day[1])
        else:
            annual[date.year] += int(day[1])

    return annual

def main():
    base_url = "https://or.water.usgs.gov/non-usgs/bes/"
    rain_files = get_rain_files(base_url)
    for i, file in enumerate(rain_files):
        print(i, file)
    choice = int(input("Which rain file? "))

    rain_file = rain_files[choice]

    rain_data = get_rain_data(base_url, rain_file)

    data = format_data(rain_data)

    rain_fall = [rain * .01 for rain in data.values()]
    pyplot.bar(list(data.keys()), rain_fall)
    pyplot.show()


main()