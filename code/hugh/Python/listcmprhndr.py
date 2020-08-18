#List comprehensions allow us to generate a list with a single statement

nums = []
for x in range(10):
    nums.append(x ** 2)
print(nums)


nums = [x ** 2 for x in range(10)]
print(nums)

words = '''a
aa
aaa
aachen
aardvark
aardvarks
aaron
aback
abacus
abacuses
abaft
abalone
abandon
abandoned
abandoning
abandonment
abandons
abase
abased
abasement
abases
abash
abashed
abasing
abate
abated
abatement
abatements
abates
abating
abattoir
abattoirs
abbess
abbesses
abbey
abbeys
abbot
abbots
abbreviate
abbreviated
abbreviates
abbreviating
abbreviation
abbreviations
abc'''

words = words.split('\n')

long_words = [word for word in words if len(word)>5]

print(long_words)

numbers = '133425453'

intnumbslist = [int(num) for num in numbers]
print(intnumbslist)

'''REPL = read evaluate print loop'''

def dictionizer(numbers, target):
    numbdict = {numbers,target}
    for i in range(len(numbers)):
       numbdict.update(dict(list(i) + list(numbers))

print(dictionizer(numbers,20))