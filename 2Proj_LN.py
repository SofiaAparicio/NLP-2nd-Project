################################################
#                   imports                    #
################################################
import nltk
from nltk import tokenize
import codecs


################################################
#                 functions                    #
################################################
def run():
    with codecs.open("virVerVir-1.final", "r", "latin-1") as file:
        raw = (file.read())#.split('\n')#.decode('utf-8')
    file.close()

    tokens = tokenize.word_tokenize(raw, language = "portuguese")
    #see unigrams
    tokens = [token.lower() for token in tokens]

    unigrams = [(item, tokens.count(item)) for item in sorted(set(tokens))]
    for un in unigrams:
        print (un[0]).encode('utf-8')
    #Create your bigrams
    bgs = nltk.bigrams(tokens)

    #compute frequency distribution for all the bigrams in the text
    fdist = nltk.FreqDist(bgs)
    # print("Frequency distribution for bigrams")
    # for k,v in fdist.items():
    #     print(k,v)
run()
