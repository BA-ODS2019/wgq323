# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:50:41 2019

@author: Christian Laursen
"""

import os
from scipy import stats
from nltk.probability import FreqDist
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Ændrer antal kolonner og bredde så dataframen nemmere kan læses.
pd.set_option('display.max_columns', 8)
pd.set_option('display.width', 150)

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

#Creating text lists based on different dates
#Also creating strings with all the texts from each period (used for wordclouds later)
list1 = []
text1 = ' '
list2 = []
text2= ' '
list3 = []
text3= ' '
list4 = []
text4= ' '

for i,file in enumerate(dates):
    with open((directory+"/"+dates[i]), encoding='utf-8') as handle: 
        text = "\n".join([x.strip() for x in handle])
        if 1930 < int(dates[i][-12:-8]) <1960:
            list1.append(text.lower())
            text1 += text.lower() + ' '
        if 1959 < int(dates[i][-12:-8]) <1990:
            list2.append(text.lower())
            text2 += text.lower() + ' '
        if 1989 < int(dates[i][-12:-8]) <2000:
            list3.append(text.lower())
            text3 += text.lower() + ' '
        if 1999 < int(dates[i][-12:-8]) <2020:
            list4.append(text.lower())
            text4 += text.lower() + ' '
            
#Number of texts:
len(files)

#Dataframe to contain data of each time period
period = []
awlength = []
aplength = []
atlength = []
anpt = []

period.append('All')
period.append('1930-1959')
period.append('1960-1989')
period.append('1990-1999')
period.append('2000-2019')


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
   
# Average paragraph length:
def paralength(list_of_texts):
    listlength = 0
    amount_of_p = 0
    for d,text in enumerate(list_of_texts):
        paragraphs = text.split("\n")
        listlength += len(text)
        for paragraph in paragraphs:
            amount_of_p += 1
    aplength.append(listlength/amount_of_p)
    print("Average paragraph length in this list of texts:",listlength/amount_of_p)  

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
    return total_length/len(list_of_words)

#Average text lenght:
def textlength(list_of_texts):
    textlength = 0
    for text in list_of_texts:
        textlength += len(text)
    atlength.append((textlength/len(list_of_texts)))
    print("Average text length:",(textlength/len(list_of_texts)))
        
# Open a file with danish stopwords, and saving it in a list
f = open("data/stopord.txt", encoding="UTF-8")
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
    print("Average word length with stopwords:",averagelength(wordlist(list_of_texts)))
    print("Average word length without stopwords:",  averagelength(remove(wordlist(list_of_texts))))
    awlength.append(averagelength(remove(wordlist(list_of_texts))))
    textlength(list_of_texts)

# Counting the amount of paragraphs
def paragraph(list_of_texts):
    chars = []
    for text in list_of_texts:
        for char in text:
            chars.append(char)
    print("Paragraphs in this list of texts:",chars.count("\n"))
    anpt.append((chars.count("\n")/len(list_of_texts)))
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

# Putting all text from each document into a single string  
alltext = ' '
for text in files:
    alltext += text+' '

# Function to create wordclouds
"""
Run these command lines in command prompt
pip install matplotlib
pip install pandas
pip install wordcloud
"""
def wc(text):
    wordcloud = WordCloud(width = 600, height = 600, 
                    background_color ='white', 
                    stopwords = stopord, 
                    min_font_size = 10).generate(text)
    
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0)   
    plt.show()

print("\nAll the texts:")
printInfo(files)
wc(alltext)
print("\nTexts from 1930-1959:")
printInfo(list1)
wc(text1)
print("\nTexts from 1960-1989:")
printInfo(list2)
wc(text2)
print("\nTexts from 1990-1999:")
printInfo(list3)
wc(text3)
print("\nTexts from 2000-2010:")
printInfo(list4)
wc(text4)

#Creating a dataframe with data from each time period
df = pd.DataFrame()
df['Period'] = period
df['Average_word_length(without_Stopwords'] = awlength
df['Average_paragraph_length'] = aplength
df['Average_text_length'] =atlength
df['Average_number_of_paragraphs_pr_text']=anpt
print(df.head())

"""
# Creating a list with the file's date and length
for i, text in enumerate(dates):
    dates[i] = text[-12:]
text_lengths = []
for i, file in enumerate(files):
    text_lengths.append(len(file))
    # print("Filename:",dates[i],"length:",len(file))  
dl = list(zip(dates,text_lengths))
dl.sort()
"""

# Bar charts showing average paragraph length and average number of paragraphs pr. text of each time period
ax = df.plot.bar(x='Period',y=['Average_paragraph_length','Average_number_of_paragraphs_pr_text'], rot=0, subplots = True)




