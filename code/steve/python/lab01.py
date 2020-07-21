# Today I went to the zoo. I saw a(n)
# ___________(adjective)
# _____________(Noun) jumping up and down in its tree.
# He _____________(verb, past tense) __________(adverb)
# through the large tunnel that led to its _______(adjective)
# __________(noun). I got some peanuts and passed
# them through the cage to a gigantic gray _______(noun)
# towering above my head. Feeding that animal made
# me hungry. I went to get a __________(adjective) scoop
# of ice cream. It filled my stomach. Afterwards I had to
# __________(verb) __________ (adverb) to catch our bus.
# When I got home I __________(verb, past tense) my
# mom for a __________(adjective) day at the zoo. 
import string

def user_inputs():
    adjective01 = input('Please enter an Adjective: ')
    noun01 = input('Please enter a noun: ')
    verb01 = input('Please enter a past tense verb: ')
    adverb01 = input('Please enter an adverb: ')
    adjective02 = input('Please enter an adjective: ')
    noun02 = input('Please enter a noun: ')
    noun03 = input('Please enter a noun: ')
    adjective03 = input('Please enter an adjective: ')
    verb02 = input('Please enter a verb: ')
    adverb02 = input('Please enter an adverb: ')
    verb03 = input('Please enter a past tense verb: ')
    adjective04 = input('Please enter an adjective: ')

    madlib = """Today I went to the zoo. I saw a 
        {adjective01} {noun01} jumping up and down in its tree.
        He {verb01} {adverb01}
        through the large tunnel that led to its {adjective02} 
        {noun02}. I got some peanuts and passed
        them through the cage to a gigantic gray {noun03}
        towering above my head. Feeding that animal made
        me hungry. I went to get a {adjective03} scoop
        of ice cream. It filled my stomach. Afterwards I had to
        {verb02} {adverb02} to catch our bus.
        When I got home I {verb03} my
        mom for a {adjective04} day at the zoo. """

    return madlib

def main():
    user_inputs()
    answer = madlib 
    print(answer)


main()
