import requests
import re
from datetime import datetime as dt


def get_rain_files(url):

    response = requests.get("https://or.water.usgs.gov/non-usgs/bes/")
    data = response.text

    rain_files = re.findall(r"\w+\.rain", data)
    return rain_files

def get_rain_data(url, rain_file):
    response = requests.get(url+rain_file)
    data = response.text
    
    rain_data = re.findall(r"(\d{2}-[A-Z]{3}-\d{4})\s+(\d+)", data)
    return r

def format_data(data):
    annual = {}
    for day in data:
        date = srtptime(day[0], '%d-%b-%Y')
        if date.year not in annual:
            annual[date.year] = int(day[1])
        else:
            annual[date.year] += int(day[1])

    for year, tips in annual.items():
        print(f"{year}: {tips * .01}in")
    
def main():
    base_url = "https://or.water.usgs.gov/non-usgs/bes/"
    rain_files = get_rain_files(base_url)
    for i, file in enumerate(rain_files):
        print(i, file)
    choice = input("WHich rain file: ")

    rain_file = rain_files[choice]

    rain_data = get_rain_data(base_url, rain_file)

main()