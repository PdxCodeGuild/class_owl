# Convert a time given in hours and minutes to a phrase.
def time_convert():
    """
    Convert  time into a phrase
    """
    hour_list = {'1': 'one','2': 'two','3': 'three','4': 'four',
    '5': 'five', '6':'six' ,'7': 'seven','8': 'eight','9': 'nine',
    '10': 'ten','11': 'eleven', '12': 'twelve'}

    mins_list = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
    '6': 'sixty'}

    

    


    print('Welcome to the Clock-verter!')
    print('Let me convert your time into a word equivalent!')
    user_time = input("Please enter a time in the\n\
following form HH:MM:SS AM/PM or in 24 hr format: ")

    user_time = user_time.split(':')
    if len(user_time) != 3:
        print('Break')
    else:    
        hours = user_time[0]
        mins = user_time[1]
        secs = user_time[2][0:2] if len(user_time[2]) >= 2 else user_time[2][0:] + '0' * (2-len(user_time[2]))
        mod = user_time[2][2:]
        print(hours,mins,secs,mod)

    # a = hour_list[hours]
    
    # if b in mins_list:
    #     mins_list[b]



    
   
    




















if __name__ == "__main__":
    time_convert()