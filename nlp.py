from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
import re
import heapq

my_stopwords = [
    "dirimu",
    "``",
    "''",
    '“',

]

stopWords = stopwords.words("indonesian") + list(punctuation) + my_stopwords
   
def to_summarize(text, url):
    text = text.replace(".. ", ". " )
    text = text.replace(". .", ". " )
    text = text.replace(". .", ". " )
    text = text.replace(". .", ". " )
    text = re.sub(' +', ' ', text)
    text = re.sub(r'(\n\s*)+\n', '', text)
    text = re.sub(r'(\t\s*)+\t', '', text)
    
    words = word_tokenize(text)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1


    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    

    if len(sentenceValue) > 0:
        summary_sentences = heapq.nlargest(5, sentenceValue, key=sentenceValue.get)
        summary = ''
        for sentence in sentences:
            if (sentence in summary_sentences):
                summary += " " + sentence

        print("\n")
        print(url.split("/")[-1].upper())
        print(heapq.nlargest(10, freqTable, key=freqTable.get))
        print(summary)
