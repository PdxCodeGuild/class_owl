#password generator lab
# import mods
import random
import string 
pass_opt = string.ascii_letters

# welcome message
print("welcome to the password generator.")

#get info
user_len = input("how long do you want your password? ")
user_len = int(user_len)
user_pass = ""

for x in range(user_len):
    user_pass += random.choice(pass_opt)
print(user_pass)
user = input("Are you satisfied with your password? yes/no? ")


#while loop 
while user == "no":
    print("ok then lets try again.")
    for x in range(user_len):
        user_pass += random.choice(pass_opt)
    print(user_pass)
    user = input("Are you satisified with your password? yes/no ")
# end session        
    if user == "yes":
        print("Very well that ends our session.")
        break


    
    
            
        