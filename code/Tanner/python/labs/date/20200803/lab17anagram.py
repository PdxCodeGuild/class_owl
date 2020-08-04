def ana():

    str1 = input("What is your first word?: ")
    str2 = input("What is your second word?: ")

    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            print("Anagrams")
        else:
            print("Not anagrams")
    else:
        print("Not anagrams")

def pali(str1):
    str2 = ''.join(reversed(str1))
    if str1 == str2:
        print("Is palindrome")
    elif str1 != str2:
        print("not palindromes")


pali("cat")