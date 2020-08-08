import datetime


def openup():
    with open("hayden_island.rain.txt") as file:
        data = file.read().split('\n')
        print(data)
    
    headers = data[0]
    headers = headers.split(',')
    data = data[1:]

    rainD = []
    for day in data:
        rainD.append(day.split(","))

    days = []
    for rain in rainD:
        rainyC = {}
        for i in range(len(headers)):
            rainyC[headers[i]] = data[i]
        days.append(rainyC)

    return days

openup()
