def anagramma():
    """
    Write another function check_anagram that takes two 
    strings as parameters and returns True if they're anagrams of 
    eachother, False if they're not. 
    The procedure for comparing the two strings is as follow:
    """    

    print("Welcome!")
    print("I check to see if two words are anagrams!")
    
    # Ask for the user input an verify it is a word
    word1 = input("Please enter a word: ").strip()
    word2 = input("please enter a second word: ").strip()
    
    while not word1.isalpha() or not word2.isalpha():
        print('ERROR! Please only enter letters.\n')

        word1 = input("Please enter a word: ").strip()
        word2 = input("please enter a second word: ").strip()
    
    # Make pretty copies to display at the end
    pretty1 = word1
    pretty2 = word2
    
    # Strip, sort, lowercase the inputs 
    word1 = word1.replace(' ',"")
    word2 = word2.replace(' ',"")
    word1 = sorted(word1.lower())
    word2 = sorted(word2.lower())

    # Compare results
    if word1 == word2:
        print(f"Yes, {pretty1} and {pretty2} are anagrams.")

    else:
        print(f"No, {pretty1} and {pretty2} are not anagrams.")

    


if __name__ == "__main__":
    anagramma()