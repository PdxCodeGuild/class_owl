# Lab 18: Peaks and Valleys
# Define the following functions:
# peaks - Returns the indices of peaks. A peak has a lower number 
# on both the left and the right.
# valleys - Returns the indices of 'valleys'. A valley is a number 
# with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single 
# list of the peaks and valleys in order of appearance in the original data.
DATA = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaky(data):
    
    data_str = list(map(str,data))
    p_list = []

    for x in range(1, len(data_str)-1):
        y = int(data_str[x-1])
        z = int(data_str[x+1])
        a = int(data_str[x])

        if y < a > z:
            p_list.append(x)

    return p_list




def vals(data):

    data_str = list(map(str,data))
    v_list = []

    for x in range(1, len(data_str)-1):
        y = int(data_str[x-1])
        z = int(data_str[x+1])
        a = int(data_str[x])

        if y > a < z:
            v_list.append(x)
    
    return v_list


def peaks_and_valleys():

    peaks = peaky(DATA)
    palleys = peaks.copy()
    valleys = vals(DATA) 

    print(f'Peaks: {peaks}')
    print(f'Valleys: {valleys}')
    palleys.extend(valleys)
    palleys.sort()
    print(f"Peaks and Valleys: {palleys}")

    

if __name__ == "__main__":
    peaks_and_valleys()