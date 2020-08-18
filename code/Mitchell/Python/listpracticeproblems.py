def combine(a, b):
    c = {}
    for i in range(len(a)):
        c.update({a[i]: b[i]})

    return c



fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
#print(combine(fruits, prices)) # {'apple':1.2, 'banana':3.3, 'pear':2.1}

if c.startswith()