# -*- coding: utf-8 -*-

import os
from scipy import stats
from collections import Counter
from nltk.probability import FreqDist
import numpy as np
import matplotlib.pyplot as plt

# Opening folder of files, and saving each text
directory = 'data/danish_news_corpus'
files = []
dates = []
for file in os.listdir(directory):
    dates.append(file)
    if file.endswith(".txt"):
        filename = os.path.join(directory, file)
        with open(filename, encoding='utf-8') as handle: 
            text = "\n".join([x.strip() for x in handle])
            files.append(text.lower())

#Creating text lists based on different dates:           
list1 = []
list2 = []
list3 = []
list4 = []
for i,file in enumerate(dates):
    with open((directory+"/"+dates[i]), encoding='utf-8') as handle: 
        text = "\n".join([x.strip() for x in handle])
        if 1930 < int(dates[i][-12:-8]) <1960:
            list1.append(text.lower())
        if 1959 < int(dates[i][-12:-8]) <1990:
            list2.append(text.lower())
        if 1989 < int(dates[i][-12:-8]) <2000:
            list3.append(text.lower())
        if 1999 < int(dates[i][-12:-8]) <2020:
            list4.append(text.lower())
            
#Number of texts:
len(files)

#Total number of characters:
def chars(list_of_texts):
    length = []
    for text in list_of_texts:
        length.append(len(text))
    print("Total amount of characters:",sum(length))

#Descriptive statistics of text length 
def statistics(list_of_texts):
    text_length = []
    for text in list_of_texts:
        text_length.append(len(text))
    print("Descriptive stats:\n",stats.describe(text_length))        
   
# Count the length of each paragraph
def paralength(list_of_texts):
    listaverage = 0
    amount_of_p = 0
    for text in list_of_texts:
        paragraphs = text.split("\n")
        textaverage = 0
        for paragraph in paragraphs:
            textaverage += len(paragraph)
            amount_of_p += 1
            #print("Paragraph length:",len(paragraph))
        #print ("Average paragraph length in this text:", textaverage/len(paragraphs))
        listaverage += textaverage
    print("Average paragraph length in this list of texts:",listaverage/amount_of_p)
    
#Total words:
def wordlist(list_of_texts):
    total_words = []
    for text in list_of_texts:
        for word in text.split():
            total_words.append(word)
    return total_words
           
#Unique words:
def unique(list_of_words):
    uwords = list(set(list_of_words)) 
    print("Unique words: ",len(uwords))

#Average word length:
def averagelength(list_of_words):
    total_length = 0
    for word in list_of_words:
        total_length += len(word)
    print("Average word length: ",total_length/len(list_of_words))

def textlength(list_of_texts):
    textlength = 0
    for text in list_of_texts:
        textlength += len(text)
    print("Average text length:",(textlength/len(list_of_texts)))
        

# Open a file with danish stopwords, and saving it in a list
f = open('data/stopord.txt', encoding="UTF-8")
stopord = f.read()
stopord = stopord.split("\n")
f.close()

#Get words that are not stop-words:
def remove(list_of_words):
    iwords = []
    for word in list_of_words:
        if word not in stopord:
            iwords.append(word)
    return iwords

# Function showing freqency:
def freq(list_of_texts):
    print("Frequency with stopwords:")
    fdist = FreqDist(wordlist(list_of_texts))
    print(fdist.most_common(30),"\n")
    print("Frequency without stopwords:")
    fdist = FreqDist(remove(wordlist(list_of_texts)))
    print(fdist.most_common(30),"\n")
    fdist.plot(10,cumulative=False)
    plt.show()

# Finding frequency of specific word in list of texts    
def freqofword(texts,word):
    fdist = FreqDist(wordlist(texts))
    print(fdist[word])
    
# Function showing average wordlength      
def average(list_of_texts):
    print("Average word length with stopwords:")
    averagelength(wordlist(list_of_texts))
    print("Average word length without stopwords:")
    averagelength(remove(wordlist(list_of_texts)))
    textlength(list_of_texts)

# Counting the amount of paragraphs
def paragraph(list_of_texts):
    chars = []
    for text in list_of_texts:
        for char in text:
            chars.append(char)
    print("Paragraphs in this list of texts:",chars.count("\n"))
    print("Average number of paragraphs pr. text:",chars.count("\n")/len(list_of_texts))

# Function printing out information
def printInfo(a_list):
    print("Number of texts:",len(a_list))
    statistics(a_list)
    chars(a_list)
    freq(a_list)
    average(a_list)
    unique(wordlist(a_list))
    paragraph(a_list)
    paralength(a_list)

print("\nAll the texts:")
printInfo(files)
print("\nTexts from 1930-1959:")
printInfo(list1)
print("\nTexts from 1960-1989:")
printInfo(list2)
print("\nTexts from 1990-1999:")
printInfo(list3)
print("\nTexts from 2000-2010:")
printInfo(list4)

# Document Term Count Matrix
from sklearn.feature_extraction.text import CountVectorizer
model_vect = CountVectorizer()
# train and apply the model
data_vect = model_vect.fit_transform(files)
print('Shape: (%i, %i)' % data_vect.shape)
data_vect

# Creating a list with the file's date and length
for i, text in enumerate(dates):
    dates[i] = text[-12:]
text_lengths = []
for i, file in enumerate(files):
    text_lengths.append(len(file))
    # print("Filename:",dates[i],"length:",len(file))  
dl = list(zip(dates,text_lengths))
dl.sort()


        



