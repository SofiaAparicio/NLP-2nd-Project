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
def run():
    with codecs.open("virVerVir-1.final", "r", encoding='utf-8') as file:
        raw = (file.read())#.split('\n')#.decode('utf-8')
    file.close()

    tokens = tokenize.word_tokenize(raw, language = "portuguese")
    #see unigrams
    punctuations = list(string.punctuation) #+ list(string.digits)

    tokens = [token.lower() for token in tokens if token not in punctuations ] #if token not in punctuations
    unigrams = [(item, tokens.count(item)) for item in sorted(set(tokens))]

    f = open('unigramasVer.txt', 'w')
    for un in unigrams:
        f.write( (un[0]).encode('UTF-8') + "\t" + str(un[1]) + "\n" ) #+ "\t" + str(un[1])
    f.close()
    print len(unigrams)


    #see bigrams
    sent = tokenize.sent_tokenize(raw, language = "portuguese")
    new_bigrams = []
    for line in sent:
        tokens = tokenize.word_tokenize(line, language = "portuguese")
        tokenLine = [token.lower() for token in tokens if token not in punctuations ] #if token not in punctuations

        # bgs = nltk.bigrams(tokenLine)
        new_bigrams += list(bigrams(tokenLine))


    ordBigrams = [(item, new_bigrams.count(item)) for item in sorted(set(new_bigrams))]

    f = open('bigramasVer.txt', 'w')
    for un in ordBigrams:
        f.write( (un[0][0]).encode('UTF-8') + " " + (un[0][1]).encode('UTF-8') + "\t" + str(un[1]) + "\n" ) #+ "\t" + str(un[1])
    f.close()


    # #bigrams mal
    # tokens = tokenize.word_tokenize(raw, language = "portuguese")
    #
    # bi = list(set(bigrams(tokens)))
    # print bi
    # print len(bi)

################################################
#                     run                      #
################################################

if __name__ == '__main__':
    run()
