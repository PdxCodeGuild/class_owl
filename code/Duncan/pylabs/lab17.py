# Palindrome and anagram

#palindrome

def is_palin(string):
    
    return user_palin == user_palin[::-1]


# anagram
def anagram_checker():
    str1 = input("Enter your first word please: ")

    str2 = input("Enter your second word please: ")

    str1 = str1.lower().replace(" ", "") 
     

    str2 = str2.lower().replace(" ", "")
    

        
    if(sorted(str1) == sorted(str2)):
        print("That is an anagram. ")
    else:
        print("That is not an anagram. ")    

# both together
user_palin = ""

def main():
    user_choice = input("Would you like to check a palindrome? y/n: ")

    if user_choice == "y":    
        user_palin = input("Enter your possible Palindrome: ")
        is_palin(user_palin)

        answer = is_palin(user_palin)
        if answer:
            print("That is infact a Palindrome.")
        else:
            print("That is not a Palindrome")        
    else:
        print("Then lets check an anagram. ")

        anagram_checker()

main()        

