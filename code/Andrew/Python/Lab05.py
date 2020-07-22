# generate emoticons by assembling a 
# randomly choosing a set of eyes, a nose, and a mouth.
import random
def emo():
    counter = 0
    while counter != 5:
        # Define a list of eyes
        eyes = [";",":","X","="]
        
        # Define a list of noses
        noses = [">","o","-","^",""]
        
        # Define a list of mouths
        mouths = ["|","/","*","O","P","/","[","]"]

        # Randomly pick a set of eyes
        # Randomly pick a nose
        # Randomly pick a mouth
        # Assemble and display the emoticon
        print(f"{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}")
        counter += 1












if __name__ == "__main__":
    emo()