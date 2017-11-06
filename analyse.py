#!/usr/bin/python

# Grupo 40:
# Sofia Aparicio - n 81105
# Rodrigo Lousada - n 81115

################################################
#                   imports                    #
################################################

from nltk import tokenize
import sys
import codecs


################################################
#                 functions                    #
################################################

def createUnigrams(unigrams_file):
    unigrams_dict = {}
    with codecs.open(unigrams_file, "r", encoding='utf-8') as file:
        raw = (file.readlines())
    file.close()
    for line in raw:
        words = line.split()
        unigrams_dict.update({words[0]:int(words[1])})
    return unigrams_dict

def createBigrams(bigrams_file):
    bigrams_dict = {}
    with codecs.open(bigrams_file, "r", encoding='utf-8') as file:
        raw = (file.readlines())
    file.close()
    for line in raw:
        words = line.split()
        bigrams_dict.update({(words[0],words[1]):int(words[2])})
    return bigrams_dict

def checkAmbiguity(ambiguity_file):
    with codecs.open(ambiguity_file, "r", encoding='utf-8') as file:
        raw = (file.readlines())
    file.close()
    line = raw[1]
    words = line.split()
    ambiguity = ((raw[0].split("\n"))[0], words[0], words[1])
    return ambiguity

def readSentences(sentences_file):
    with codecs.open(sentences_file, "r", encoding='utf-8') as file:
        raw = (file.readlines())
    file.close()
    for i in xrange(len(raw)):
        raw[i] = raw[i].lower()
    return raw

def analyseSentence(sent, unigrams_dict, bigrams_dict, ambiguity, sentences, smoothing):
    words = tokenize.word_tokenize(sent, language="portuguese")

    index_ambiguity = words.index(ambiguity[0])

    bigrams_combinations = [  (words[index_ambiguity-1],ambiguity[1]) , (ambiguity[1],words[index_ambiguity+1]) , (words[index_ambiguity-1],ambiguity[2]) , (ambiguity[2],words[index_ambiguity+1]) ]
    bigrams_values = []
    for combination in bigrams_combinations:
        if combination in bigrams_dict:
            bigrams_values.append(bigrams_dict[combination])
        else:
            bigrams_dict.update({combination:0})
            bigrams_values.append(0)

    #In case the adjacent word is not present in corpus
    for word in [words[index_ambiguity-1] , words[index_ambiguity+1]]:
        if word not in unigrams_dict:
            unigrams_dict.update({word:0})
            print "Word \"" + word.encode('UTF-8') + "\" added to corpus"

    #Calculating probability for first option
    numerator_1_1 = bigrams_values[0] + smoothing
    denominator_1_1 = unigrams_dict[words[index_ambiguity-1]] + (smoothing * len(unigrams_dict))

    numerator_1_2 = bigrams_values[1] + smoothing
    denominator_1_2 = unigrams_dict[ambiguity[1]] + (smoothing * len(unigrams_dict))

    first_option_value = float(0)
    if denominator_1_1*denominator_1_2 != 0:
        first_option_value = float(float(numerator_1_1)/float(denominator_1_1)) * float(float(numerator_1_2)/float(denominator_1_2))

    #Calculating probability for second option
    numerator_2_1 = bigrams_values[2] + smoothing
    denominator_2_1 = unigrams_dict[words[index_ambiguity-1]] + (smoothing * len(unigrams_dict))

    numerator_2_2 = bigrams_values[3] + smoothing
    denominator_2_2 = unigrams_dict[ambiguity[2]] + (smoothing * len(unigrams_dict))


    second_option_value = float(0)
    if denominator_2_1*denominator_2_2 != 0:
        second_option_value = float(float(numerator_2_1)/float(denominator_2_1)) * float(float(numerator_2_2)/float(denominator_2_2))


    print "Probability option to be \"" + (ambiguity[1]).encode("UTF-8") + "\": " + str(first_option_value)
    print "Probability option to be \"" + (ambiguity[2]).encode("UTF-8") + "\": " + str(second_option_value)

    #choose which one to use
    #in case equal choose which as more occurences
    if first_option_value==second_option_value:
        if unigrams_dict[ambiguity[1]] > unigrams_dict[ambiguity[2]]:
            return ambiguity[1]
        else:
            return ambiguity[2]
    elif first_option_value > second_option_value:
        return ambiguity[1]
    else:
        return ambiguity[2]

################################################
#                     run                      #
################################################

if __name__ == '__main__':
    smoothing = 0
    if (len(sys.argv)==6 and sys.argv[5]=="use-smoothing"):
        smoothing = 1

    unigrams_file = sys.argv[1]
    bigrams_file = sys.argv[2]
    ambiguity_file = sys.argv[3]
    sentences_file = sys.argv[4]

    unigrams_dict = createUnigrams(unigrams_file)
    bigrams_dict = createBigrams(bigrams_file)

    ambiguity = checkAmbiguity(ambiguity_file)

    sentences = readSentences(sentences_file)

    for sent in sentences:
        print "Sentence nr." + str(sentences.index(sent) + 1) + ": " + sent[:-1].encode("UTF-8")
        result = analyseSentence(sent, unigrams_dict, bigrams_dict, ambiguity, sentences, smoothing)
        print "Result: " + str(result) + "\n"
