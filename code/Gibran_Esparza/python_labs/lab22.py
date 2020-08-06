#Lab22 ARI (Gibran and Tanner)

#Read in file
def read(file_name):
    with open(file_name) as cows:
        text = cows.read().lower()
    return text

#print(read("how_to_select_cows.txt"))
#Counts the words in file
def count_words(text):
    word_counts = 0

    for word in text:
        word_counts += 1
           
    return word_counts
#Count the characters in words
def count_characters(word_counts):
    charactercount = 0

    for word in word_counts:
        for character in word:
            charactercount +=1
    
    return charactercount
   
#Count Sentences in text
def count_sentences():
    ctext = read("how_to_select_cows.txt").split(".")
    
    return len(ctext)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def main():
   
   text = read("how_to_select_cows.txt").split()
   bookname = "how to select cows"
   countedwords = count_words(text)
   c_characters = count_characters(text)
   sentencecount = count_sentences()
   ari = round(4.71*(c_characters/countedwords) + 0.5*(countedwords/sentencecount)- 21.43)

   score = ari_scale[ari]

   print (f'''The ARI for {bookname} is {ari}.'
This corresponds to {score['grade_level']} level of difficulty
that is suitable fo an average person {score["ages"]}years old.

''')
main() 