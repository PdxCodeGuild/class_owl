#Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
#Handle numbers from 100-999.

#Dictionaries

ones = {
   0: '.', 1: 'one', 2: 'two', 3:'three',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine' 
}

tens = {
    2: 'twenty',3: 'thirty',4: 'fourty',5: 'fifty',
    6: 'sixty',7: 'seventy',8: 'eighty',9: 'ninety'
}

teens ={
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen' 
}


def converter(number):
    
    
    if number <= 9:
        print('Your number writes as ' + ones[number])
    elif number > 9 and number < 20 :
        print('Your number writes as ' + teens[number])
    elif number >= 20 and number < 100:
        tensd= number//10
        onesd= number % 10
        print("Your number writes as " + tens[tensd] + "-" + ones[onesd])
    elif number >= 100 and number <= 999:
        hundreds= number // 100
        tensd= number//10
        onesd= number % 10
        print("Your number writes as " + ones[hundreds] + "-" + "hundred" )
     
def main():
    
    number = int(input("Enter a number  0-999: "))

    converter(number)

main()