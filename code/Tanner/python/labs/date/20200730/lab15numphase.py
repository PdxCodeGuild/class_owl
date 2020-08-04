def converter():

    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    x = int(input("what number should we convert?: "))

    if x < 20:
        return units[x]

    elif x < 100:
        return tens[x // 10] + units[int(x % 10)]





print(converter())