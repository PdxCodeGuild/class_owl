''' This code will take in a list of numbers from the user and average them together'''
# Welcome message
print('Welcome to the averager, please input a list of integers to be averaged or any string to exit: ')

#set up the list
tobeavg= []
#set up outer loop, using exception blocks to handle all non-number entries
while True:
    #try this code block, and if you hit an error run the except code block, 
    #there could also be an else
    try:
        userinput = int()
        userinput = input()
        #setting a new value equal to the int of the input means you arent changing the original
        intuserinput = int(userinput)
        #update the list
        tobeavg.append(intuserinput)
        #get the length of the list for averaging later
        tobeavglen = len(tobeavg)
        #initialize sum value, avoiding using sum function on purpose here for lab
        addaveraged = int()
        #increment the sum value with the int input value
        addaveraged += intuserinput
    #except will handle all other errors, not great error handling experience for users
    #but very effective
    except ValueError:
        #get the final average by dividing sum value by list length 
        finalaveraged = addaveraged / tobeavglen
        #print user friendly message
        print(f'You entered a non-number, printing average of {tobeavg}')
        #print final average
        print(finalaveraged)
        #leave program
        break
