print('Come On Ya Hear! How much dollars ya got, I can make some change for ya')

def pennies():
    pennies1 = float(input('how much money do ya got, i dont need no dollar sign ya hear'))
    pennies2 = pennies1 * 100
    
    return pennies2

penniesresult = pennies()

def change_calc(penniesresult):
    quarters = penniesresult // 25
    penniesresult = penniesresult - (quarters * 25)
    dimes = penniesresult // 10
    penniesresult = penniesresult - (dimes * 10)
    nickels = penniesresult // 5
    penniesresult = penniesresult - (nickels * 5)
    penny = penniesresult // 1
    penniesresult = penniesresult - (penny * 1)
    print('You have', quarters, 'quarters, ', nickels, 'nickels, ', dimes, 'dimes, and ', penny, 'pennies')
       



change_calc(penniesresult)
