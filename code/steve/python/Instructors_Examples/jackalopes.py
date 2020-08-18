import random
import time
from matplotlib import pyplot

STARTING_POP = 2
GOAL_POP = 10000
LIFE_EXPECTANCY = 10
BREEDING_YEARS = [2, 8]


def generate_name(length = 4):
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"

    name = ""
    for i in range(length):
        if i % 2:
            name += random.choice(vowels)
        else:
            name += random.choice(consonants)
    return name




class Jackalope:

    def __init__(self, name, gender):
        self.name = name
        self.age = 0
        self.gender = gender
        self.is_pregnant = False

    def __str__(self):
        return f"({self.gender[0]}){self.name} {self.age} {self.is_pregnant}"

    def birthday(self):
        self.age += 1

    def is_dead(self):
        return self.age > LIFE_EXPECTANCY

    def mate(self):
        if self.gender == "female":
            if BREEDING_YEARS[0] <= self.age <= BREEDING_YEARS[1]:
                self.is_pregnant = True


def age_jackalopes(jackalopes):
    for jackalope in jackalopes:
        jackalope.birthday()

    return jackalopes

def remove_jackalopes(jackalopes):
    for jackalope in jackalopes:
        if jackalope.is_dead():
            jackalopes.remove(jackalope)

    return jackalopes

def mate(jackalopes):
    for i in range(len(jackalopes)-1 ):
        this_joey = jackalopes[i]
        next_joey = jackalopes[i + 1]

        if this_joey.gender != next_joey.gender:
            if not this_joey.is_pregnant and not next_joey.is_pregnant:
                this_joey.mate()
                next_joey.mate()
    return jackalopes


def gestate(jackalopes):
    for jackalope in jackalopes:
        if jackalope.is_pregnant:
            jackalope.is_pregnant = False
            jackalopes.append(Jackalope(generate_name(), random.choice(["male", "female"])))
            jackalopes.append(Jackalope(generate_name(), random.choice(["male", "female"])))

    return jackalopes


def main():
    

    jackalopes = []
    for i in range(STARTING_POP):
        name = generate_name()
        if i % 2:
            jackalopes.append(Jackalope(name, "female"))
        else:
            jackalopes.append(Jackalope(name, "male"))
    years = []
    pop_over_time = []
    year = 0
    population = len(jackalopes)
    while population < GOAL_POP:
        years.append(year)
        pop_over_time.append(population)
        # time.sleep(.5)
        year += 1

        # If jackalope is pregnant, have a baby... or two
        jackalopes = gestate(jackalopes)

        # Ages all jackalopes by 1 year
        jackalopes = age_jackalopes(jackalopes)
        
        # Removes any jacklopes that are over 10 years old
        jackalopes = remove_jackalopes(jackalopes)

        # Determine if jackalopes should mate
        jackalopes = mate(jackalopes)

        random.shuffle(jackalopes)

        # time.sleep(1)
        # for jackalope in jackalopes:
        #     print(jackalope)

        population = len(jackalopes)
        if population < 2:
            print("All jackalopes died :(")
            break


    print(year, population)
    pyplot.plot(years, pop_over_time)
    pyplot.show()


main()