################################################
#                   imports                    #
################################################
import nltk
from nltk import tokenize
from nltk.util import ngrams, bigrams
import codecs
import string

################################################
#                 functions                    #
################################################

def unigramsGenerator(verb, raw):
    tokens = tokenize.word_tokenize(raw, language = "portuguese")
    punctuations = list(string.punctuation) #+ list(string.digits)
    tokens = [token.lower() for token in tokens if token not in punctuations ] #if token not in punctuations
    unigrams = [[item, tokens.count(item)] for item in sorted(set(tokens))]

    f = open(verb + 'Unigramas.txt', 'w')
    for un in unigrams:
        f.write( (un[0]).encode('UTF-8') + "\t" + str(un[1]) + "\n" )
    f.close()

def bigramsGenerator(verb, raw):
    sent = tokenize.sent_tokenize(raw, language = "portuguese")
    punctuations = list(string.punctuation) #+ list(string.digits)
    new_bigrams = []

    for line in sent:
        tokens = tokenize.word_tokenize(line, language = "portuguese")
        tokenLine = [token.lower() for token in tokens if token not in punctuations ] #if token not in punctuations

        # bgs = nltk.bigrams(tokenLine)
        new_bigrams += list(bigrams(tokenLine))

    ordBigrams = [[item, new_bigrams.count(item)] for item in sorted(set(new_bigrams))]

    f = open(verb + 'Bigramas.txt', 'w')
    for bi in ordBigrams:
        f.write((bi[0][0]).encode('UTF-8') + " " + (bi[0][1]).encode('UTF-8') + "\t" + str(bi[1]) + "\n")
    f.close()

def main(filename, verb):
    with codecs.open(filename, "r", encoding='utf-8') as file:
        raw = (file.read())#.split('\n')#.decode('utf-8')
    file.close()

    unigrams = unigramsGenerator(verb, raw)
    bigrams = bigramsGenerator(verb, raw)

################################################
#                     run                      #
################################################

if __name__ == '__main__':
    main("virVerVir-1.final", "vir")
    main("foraIrSer-2.final", "fora")
