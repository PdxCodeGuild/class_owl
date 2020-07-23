# Write a simple program that prompts the user for several
#  inputs then prints a Mad Lib as the result.
def Madlib():
    """I forgot about Doc Strings
    """
    adj1 = input('Enter an Adjective: ')
    animal1 = input('Enter an Animal: ')
    verb_past = input('Enter a past tense verb: ')
    adv = input('Enter an Adverb: ')
    adj2 = input('Enter another Adjective: ')
    noun1 = input('Enter a Noun: ')
    animal2 = input('Enter another animal: ')
        
    print(f"""Today I went to the zoo. I saw a {adj1} {animal1} jumping up and down in its tree. He {verb_past} {adv} through the large tunnel that led to its {adj2} {noun1}. I got some peanuts and passed them through the cage to a gigantic gray {animal2} towering above my head. Feeding that animal made me hungry.""")



if __name__ == "__main__":
    
    Madlib()







