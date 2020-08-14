
words = """a
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
abc"""


words = words.split('\n')

# nums = []
# for x in range(10):
#     nums.append(x ** 2)

# nums = [x**2 for x in range(10)]


# long_words = [word for word in words if len(word) > 5]
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
# print(long_words)


numbers = "123456789"
int_numbers = [int(x) for x in numbers]
# print(int_numbers)


number = 4

result = "Dogs are cute" if 4 < 2 else "Dogs are still cute" if "banana" == "cucumber" else "cats are cute"
print(result)