# Cypher a string input from user with following cypher:
'''
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
'''
import string
cypher = string.ascii_lowercase

#set our global variables
rotamount = int()
userstring = str()

#define rotation function
def rotate(userstring,rotamount):
    stringlist = list(userstring)
    for letters in stringlist:
        lettersint = (cypher.find(letters) + rotamount)%26
        for x in stringlist:
            x = cypher.find(lettersint)
        print(stringlist)
        return str(stringlist)

# welcome user
print('Welcome to the Rotation Cypher!')
#get input
userstring = input('Please enter your string to be rotated: ').lower
#get rotation amount, default to 13
rotamount = int()
while True:
    try:
        rotamount = int(input('Please enter a rotation amount, it will default to 13: '))
    except ValueError:
        rotamount = 13
        print(f'Your string cyphered {rotamount} is {rotate(userstring,rotamount)}')
        break
    else:
        print(f'Your string cyphered {rotamount} is {rotate(userstring,rotamount)}')
        break