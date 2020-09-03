''' This code is meant to 

# Crime Data

Open one of the crime data csv's in the data folder, and derive the following statistics.

- The specific most common crime type.
- The rarest crimes.
- The year with the most crime.

'''
#modules and stuff
import re

#crime dictionary, print crimes into
crimedict = {}

# Read in the file
def getfile(file):
    #open the file and store it as data
    with open(file) as data:
        #read data in as lines
        data = data.readlines()
        #pull out headers to use later
        headers = data[0]
        #get data minus headers
        dataminusheaders = data[1:]
        #we will use findall method from RE to find everything between quotes
        for crimes in dataminusheaders:
            incident = re.findall(r"\"([a-zA-Z0-9/: ,-\.]+)\"", crimes)
            #check if in dict, if not set to one
            if incident[3] not in crimedict:
                crimedict.update({incident[3]:1})
            #if in dict then add one to this count, will not average larceny and larceny grand
            else:
                crimedict[incident[3]]+=1
    return crimedict

#Processcrimedata will get the most common and rare crimes from the data put into it using the begining of the list and iterating through
def processcrimedata(crimefiles):
    data = getfile(crimefiles)
    #get most common crime based on data using index 0 as start of list
    mostcommon = list(data.items())[0]
    rarecrime = list(data.items())[0]
    for crimes in list(data.items()):
        if crimes[1] > mostcommon[1]:
            mostcommon = crimes
        elif crimes[1] < rarecrime[1]:
            rarecrime = crimes
    return {
        "rare":rarecrime,
        "common": mostcommon,
        "total": sum(data.values())
        }

#main
def main ():
    print('Welcome to Crime Stat!')
    #pul in data sets
    data1 = processcrimedata("crime_incident_data_2011.csv")
    data2 = processcrimedata("crime_incident_data_2012.csv")
    data3 = processcrimedata("crime_incident_data_2013.csv")
    data4 = processcrimedata("crime_incident_data_2014.csv")
    #print data sets and assign year values
    print(f'2011 Stats{data1}\n,2012 Stats{data2}\n,2013 Stats{data3}\n,2014 Stats{data4}')

main()






# Most common specific crime

# Rarest Crimes

# Year with most crimes

# Pull out special characters