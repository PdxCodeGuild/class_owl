# lab 9 unit converter
# welcome message
print("Welcome to the unit converter.")
# get input   
distance = input("what unit would you like to convert to meters? acceptable choices are feet, miles, meters, kilometers, yard, inch." )
dist = int(input(f"how many{distance} would you like to convert? ")) 

#convert to meters
if distance == "feet":
    print(f"{dist} {distance} is equal to {dist * 0.3048}")
elif distance == "miles":
    print(f"{dist} {distance} is equal to {dist * 1609.34}")
elif distance == "meters":
    print(f"{dist} {distance} is equal to {dist * 1}")
elif distance == "kilometers":
    print(f"{dist} {distance} is equal to {dist * 1000}")
elif distance == "yard":
    print(f"{dist} {distance} is equal to {dist * 0.9144}")    
elif distance == "inch":
    print(f"{dist} {distance} is equal to {dist * 0.0254}")
    
#print result





