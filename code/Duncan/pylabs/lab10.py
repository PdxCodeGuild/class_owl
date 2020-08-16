# lab 10 average numbers

# get numbers from user and convert to list


# convert string list to int list

# get sum of numbers
nums_list = []
nums = input("Enter a number or done if done: ")
while True:
    if nums.isdigit():
        nums_list.append(nums)
        print(nums_list)
        nums = input("Enter a number or done if done: ")

    elif nums == "done":
        nums_list = [int(x) for x in nums_list]
        avg = sum(nums_list) / len(nums_list)
        print(f"your average is: {avg}" )
       
        break

        
            
   
        
        

           
    
        
    
    
                         
        
        
            
        



