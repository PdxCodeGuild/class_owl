'''
Lab: Sock Sorter
You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.

Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']

Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.

Version 2
Now you have a mix of types and colors. Represent socks using tuples containing one color and one type ('black', 'crew'). Randomly generate these, and then group them into pairs.

sock_colors = ['black', 'white', 'blue']
'''



# Import random
import random

# Generate socks
def sock_gen(num=100):
    sock_types = ['ankle', 'crew', 'calf', 'thigh']
    colors = ['black', 'white', 'blue', 'yellow']
    
    socks = []

    for i in range(num):
        socks.append((random.choice(sock_types), random.choice(colors)))

    # socks = [random.choice(['ankle', 'crew', 'calf', 'thigh']) for i in range(num)]

    return socks


# Sort socks into pairs
def sort_socks(socks):

    pairs = {}

    for sock in socks:
        if sock in pairs:
            pairs[sock] += 1
        elif sock not in pairs:
            pairs[sock] = 1

    return pairs



def main():
    socks = sock_gen(100)

    # print(socks)
    sorted_socks = sort_socks(socks)
    print(sorted_socks)

    for pair in sorted_socks:
        print(f"{pair}: {sorted_socks[pair]//2} pairs.")


main()