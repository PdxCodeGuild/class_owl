def dub(entry):
    dubstr = ""
    for x in entry:
        dubstr += x*2
    return dubstr

def missing(string):
    l = []

    for i in range(len(string)):
        subset = string[:i] + string[i + 1:]
        l.append(subset)
    return l



print(missing("cat"))