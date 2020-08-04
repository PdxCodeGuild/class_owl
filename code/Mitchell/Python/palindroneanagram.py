

def palindrome():
    print("\n\tAnagram-Automatic ")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word1 = input("\tCheck to see if your word is a palindrome! \n\tEnter the word now   ").replace(" ", "").replace(punctuations, '')
    

    palindrome1 = word1.lower()
    palindrome2 = word1[::-1]

    if palindrome1 == palindrome2:
        print("true palindrome")
    else:
        print("false palindrome")





def anagram():
    print("\n\tAnagram-Automatic ")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word1 = input("\tCheck to see if your two words are anagrams! \n\tEnter the First word now   ").replace(" ", "").replace(punctuations, '')
    word2 = input("\tEnter the Second Word!").replace(" ", "").replace(punctuations, '')



    anagram_list1 = (f'The firs word\'s made up of = {list(word1)}').lower()
    anagram_list2 = (f'The second is made up of    = {list(word2)}').lower()
    print(anagram_list1, anagram_list2)

    if (sorted(anagram_list1)) == (sorted(anagram_list2)):
        print("They are anagrams!")
    elif (sorted(anagram_list1)) != (sorted(anagram_list2)):
        print("Your words are not anagrams") 

palindrome()