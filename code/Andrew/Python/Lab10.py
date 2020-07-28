def running_sum():
    """
    Adds sums in an array
    """
    # Running sum
    run_sum = 0
    
    # Array of numbers
    nums = []

    # User input baseline for breaking loop later:
    user_input = ''

    print('Welcome! Weary traveller!')

    # Main loop
    while True:
        
        # User input and verification
        user_input = input("Please enter a number or enter 'done' to exit: ")
        try:
            user_input = int(user_input)

        except ValueError:
            if user_input != 'done':
                print('Please only enter integers!')
            else:
                break
        else:
            if user_input != 'done':
                run_sum += user_input
                nums.append(user_input)    
    
    print(f'Goodbye! Your Average was {run_sum/len(nums) if len(nums)> 0 else "n/a"}')
    







if __name__ == "__main__":
    running_sum()