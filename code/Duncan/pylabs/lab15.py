#  Number to phrase
# import 
import string
# create dictionary 
nums_key = { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
    19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 
    50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 
    90: 'Ninety', 100: 'One hundered', 200: 'Two hundred', 300: 'Three hundred',
    400: 'Four hundred', 500: ' Five hundred', 600: 'Six hundred',
    700: 'Seven hundred', 800: 'Eight hundred', 900: 'Nine hundred', 0: 'Zero' 
}

# get input
user_num = int(input("Enter a number: "))
# used exceptions as function
try:
    print(nums_key[user_num])
except KeyError:
    try:
        print(nums_key[user_num - user_num %10] +  nums_key[user_num %10].lower())
    except KeyError:
        try:
            print(nums_key[user_num //100 *100] +  "-" + nums_key[user_num //10 %10 *10].lower() + "-" + nums_key[user_num %10].lower())            
        except KeyError:
            print("Number out of range.")
                  