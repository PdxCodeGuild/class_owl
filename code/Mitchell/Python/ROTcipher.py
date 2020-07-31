import string
print("\t\t Welcome to the Roman Times! \n \t\t We have to encode everything we write")
text = input("\t\t Write a phrase to cipher!  ")
shift = int(input("\t\tHow many spaced do you wish to shift the cipher?  "))


def caesar(text, shift): 
    rot = ""
    for ch in text:
        if ch.isalpha():
            rot_text = ord(ch) + shift 
            if rot_text > ord('z'):
                rot_text -= 26
            finalCipher = chr(rot_text)
        
        rot += finalCipher

    print ("Your Cipher is: " + "\n\t" + rot)

    return rot

caesar(text, shift)