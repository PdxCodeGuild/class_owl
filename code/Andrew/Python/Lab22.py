# Imports math module so we can use math.ceil
import math

# Global dictionary

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

# Opening book function
def get_book(book):
    
    # Read returns strings, readlines returns a list and readline reads only the first line
    with open(book) as book:
        lines = book.read()

    return lines


def main():
    

    # Passes book title to the open function and retrieves the info as a string
    lines = get_book('book.txt')

    # s = {"?" : ".",
    #       "!": "."}
    # w = str.maketrans(s)
    # d = lines.translate(w)

    # Remove the '?' and '!' from the text. Alternate version is above and commented out
    no_ex = lines.replace('!', ".")
    no_ques = no_ex.replace("?", ".")

    # Gets the amount of sentences in the book
    sentences = len(no_ques.split('.'))

    # gets rid of the spaces and counts the letters
    chars = len(lines.replace(' ', ""))

    # Splits on spaces and counts the words
    words = len(lines.split(' '))


    # Does the math equation 
    chunk_1 = 4.71*(chars/words) 
    chunk_2 = chunk_1 + (.5 * (words/sentences)) 
    chunk_3 = math.ceil(chunk_2 - 21.43)


    # Takes the resultant and gets the 1st layer dictionary
    result_dict = ari_scale.get(chunk_3)


    # Prints the result and the info from the second layer of the dictionary

    print(f"""
The ARI for book.txt is {chunk_3}
This corresponds to a {result_dict['grade_level']} of difficulty
that is suitable for an average person {result_dict['ages']} years old.
""")

# Adding Lab22 by: Andrew, Duncan and Hugh!

if __name__ == "__main__":
    main()