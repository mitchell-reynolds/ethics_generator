import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def main(book):
    with open(r"./texts/remove_punct/{:}.txt".format(book), 'r', encoding="utf8") as inFile, \
            open(r"./texts/remove_stop_words/{:}.txt".format(book), 'w', encoding="utf8") as outFile:
        stop_words = set(stopwords.words('english'))
        for line in inFile.readlines():
            words = word_tokenize(line)
            filtered_words = " ".join(w for w in words if w not in stop_words)
            outFile.write(filtered_words + '\n')

if __name__ == '__main__':
    main(book="morals")
    main(book="ethics")
