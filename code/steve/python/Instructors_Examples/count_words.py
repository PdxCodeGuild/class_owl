from string import punctuation

def excluded_words():
    STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    EXCLUDE = []
    for word in STOPWORDS:
        if "'" in word:
            word = word.replace("'", "")
        EXCLUDE.append(word)
    return EXCLUDE


def read_file(file_name):
    with open(file_name) as cows:
        text = cows.read().lower()
    return text

def clean_text(text):
    for char in text:
        if char in punctuation:
            text = text.replace(char, "")

    text = text.replace("\n", " ")

    text = text.split(" ")

    clean_text = []
    for word in text:
        if not word.isdigit() and word != "":
            clean_text.append(word)

    return clean_text

def count_words(clean_text, excluded_words = []):
    word_counts = {}

    for word in clean_text:
        if word not in excluded_words:
            if word not in word_counts:
                word_counts.update({word: 1})
                # word_counts[word] = 1
            else:
                word_counts[word] += 1
    return word_counts

def count_pairs(clean_text):
    pair_counts = {}

    for i in range(len(clean_text) - 1):
        word = clean_text[i]
        next_word = clean_text[i + 1]
        word_pair = f"{word} {next_word}"
        if word_pair not in pair_counts:
            pair_counts.update({word_pair: 1})
        else:
            # pair_counts.update({word_pair: pair_counts.get(word_pair) + 1})
            pair_counts[word_pair] += 1

    return pair_counts

def user_pairs(word, pairs):
    user_counts = {}
    for pair in pairs:
        if pair.startswith(word):
            user_counts[pair] = pairs[pair]
    return user_counts

def top_ten(word_counts):
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_counts.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

def main():
    excluded = excluded_words()
    text = read_file("how_to_select_cows.txt")
    sanitized_text = clean_text(text)
    counted_words = count_words(sanitized_text, excluded)
    counted_pairs = count_pairs(sanitized_text)
    word = input("Enter a word to search: ")
    user_count = user_pairs(word, counted_pairs)
    # top_ten(counted_words)
    # top_ten(counted_pairs)
    top_ten(user_count)

main()