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
    unigrams_dict = {}
    tokens = tokenize.word_tokenize(raw, language = "portuguese")
    punctuations = list(string.punctuation) #+ list(string.digits)
    tokens = [token.lower() for token in tokens if token not in punctuations ] #if token not in punctuations
    unigrams = [[item, tokens.count(item)] for item in sorted(set(tokens))]

    f = open('unigramas' + verb + '.txt', 'w')
    for un in unigrams:
        unigrams_dict.update({un[0]:un[1]})
        f.write( (un[0]).encode('UTF-8') + "\t" + str(un[1]) + "\n" )
    f.close()

    return unigrams_dict

def unigramsSmoother(verb, unigrams):
    unigrams_smoothed = unigrams
    for un in unigrams_smoothed:
        un[1] += len(unigrams_smoothed)

    f = open('unigramas' + verb + 'Smoothed.txt', 'w')
    for un in unigrams_smoothed:
        f.write( (un[0]).encode('UTF-8') + "\t" + str(un[1]) + "\n" )
    f.close()

    return unigrams_smoothed

def bigramsGenerator(verb,raw):
    sent = tokenize.sent_tokenize(raw, language = "portuguese")
    punctuations = list(string.punctuation) #+ list(string.digits)
    new_bigrams = []
    for line in sent:
        tokens = tokenize.word_tokenize(line, language = "portuguese")
        tokenLine = [token.lower() for token in tokens if token not in punctuations ] #if token not in punctuations

        # bgs = nltk.bigrams(tokenLine)
        new_bigrams += list(bigrams(tokenLine))


    ordBigrams = [[item, new_bigrams.count(item)] for item in sorted(set(new_bigrams))]

    f = open('bigramas' + verb + '.txt', 'w')
    for bi in ordBigrams:
        f.write( (bi[0][0]).encode('UTF-8') + " " + (bi[0][1]).encode('UTF-8') + "\t" + str(bi[1]) + "\n" )
    f.close()

    return ordBigrams

def bigramsSmoother(verb, bigrams):
    bigrams_smoothed = bigrams
    for bi in bigrams_smoothed:
        bi[1] += 1

    f = open('bigramas' + verb + 'Smoothed.txt', 'w')
    for bi in bigrams_smoothed:
        f.write( (bi[0][0]).encode('UTF-8') + " " + (bi[0][1]).encode('UTF-8') + "\t" + str(bi[1]) + "\n" )
    f.close()

    return bigrams_smoothed

def main(filename, verb):
    with codecs.open(filename, "r", encoding='utf-8') as file:
        raw = (file.read())#.split('\n')#.decode('utf-8')
    file.close()

    unigrams = unigramsGenerator(verb, raw)
    unigrams_smoothed = unigramsSmoother(verb, unigrams)

    bigrams = bigramsGenerator(verb, raw)
    bigrams_smoothed = bigramsSmoother(verb, bigrams)

################################################
#                     run                      #
################################################

if __name__ == '__main__':
    main("virVerVir-1.final", "Vir")
    main("foraIrSer-2.final", "Fora")
