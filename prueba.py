import nltk
import os

os.getcwd()
text_file = open(r"C:\Users\PC\Documents\Markov\DCfrances.txt","r")

p = text_file.read()
words = nltk.tokenize.word_tokenize(p)

fdist= nltk.FreqDist(words)
print(len(words))
