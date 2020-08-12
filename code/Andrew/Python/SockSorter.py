
import random

def socks():
    temp = []
    for _ in range(100):
        style = random.choice(['ankle', 'crew', 'calf', 'thigh'])
        color = random.choice(['black', 'white', 'blue'])
        temp.append((style,color))
    
    return temp

def sockounter(socks):
    temp = {}
    for x in socks:
        if x not in temp:
            temp.update({x:1})
        else:
            temp[x] +=1
    
    return temp
    





def socker():
    sock_list = socks()
    counted_socks = sockounter(sock_list)

    for key, value in counted_socks.items():
        pairs, loners = divmod(value,2)
        print(f'{key} : {pairs} pairs and {loners} loners.')        




if __name__ == "__main__":
    socker()