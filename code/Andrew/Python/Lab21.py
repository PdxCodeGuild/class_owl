STOPWORDS = ['I','and','And', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def word_herder():

    import string

    translator = str.maketrans('', '', string.punctuation)
    
    all_dem = {}

    with open('Book.txt','r') as book:
        
        l = book.readlines()
        r = ''.join(l).translate(translator)
        print(r)
        r = r.split(' ')

        for word in r:
            if word in " \n":
                continue
            elif word.lower() in STOPWORDS or word in STOPWORDS:
                continue
            elif word not in all_dem:
                all_dem.update({word:1})
            else:
                all_dem[word] +=1
            

        # for x in range(4352):
        #     s = book.readline().translate(translator)
            
        #     for word in s.split(' '):
        #         if word in " \n":
        #             continue
        #         elif word.lower() in STOPWORDS or word in STOPWORDS:
        #             continue
        #         elif word not in all_dem:
        #             all_dem.update({word:0})
        #         else:
        #             all_dem[word] +=1
            
            

    

    words = list(all_dem.items()) # .items() returns a list of tuples

    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])






if __name__ == "__main__":
    word_herder()