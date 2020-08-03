#pick6
# import mods
import random




# func for generating winning pick6
def ticket():
    pick6 = []
    x = 0
    while x < 6 :
        pick6.append(random.randint(0,99))
        x += 1
    
    return pick6

    



# func for generating other tickets (not used found better solution)
# def pick6():
#     for i in range(6):
#         pick6.append(random.randint(1, 99))
#     return pick6
         

    
#   func for comparing tickets  
def compare(winning_ticket, baught_tick):
    wins = 0
    for x in range(len(winning_ticket)):
        if winning_ticket[x] == baught_tick[x]:
            wins += 1
        
        
    return wins    





# func for calc winnings (found better solution)
# def winnings():
#     pass
#     income = 0
#     if pick6[0] == pick6[0]:
#         income += 4
#     elif pick6[1] == pick6[1]:
#         income += 7
#     elif pick6[2] == pick6[2]:
#         income += 100
#     elif pick6[3] == pick6[3]:
#         income += 50000
#     elif pick6[4] == pick6[4]:
#         income +=1000000 
#     elif pick6[5] == pick6[5]:
#         income += 25000000
#     return income
     









# main prog
def main():
    tickets = 100000
    balance = 0
    earnings = 0
    winning_ticket = ticket()
    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }


    x = 0
    while x < tickets:
        x += 1
        baught_tick = ticket()
        balance -= 2

        matches = compare(winning_ticket, baught_tick)

        if matches == 1:
            balance += 4
            earnings += 4
            results[1] += 1
        elif matches == 2:
            balance += 7
            earnings += 7
            results[2] += 1
        elif matches == 3:
            balance += 100
            earnings += 100
            results[3] += 1
        elif matches == 4:
            balance += 500000
            earnings += 500000
            results[4] += 1
        elif matches == 5:
            balance += 1000000
            earnings += 1000000
            results[5] += 1                
        elif matches == 6:
            balance += 25000000
            earnings += 25000000
            results[6] += 1
        else:
            results[0] +=1 

    expenses = 100000 * 2
    roi = (earnings - expenses) / expenses           
    print(f"""
    no match: {results[0]}
    one match: {results[1]}
    two match: {results[2]}
    three match: {results[3]}
    four match: {results[4]}
    five match: {results[5]}
    six match: {results[6]}""")        
    print(f"Ending balance is: {balance=}")
    print(f"Return on investment is: {roi}")
    
   
    

main()    
