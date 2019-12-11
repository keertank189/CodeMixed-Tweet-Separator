#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:07:07 2017

@author: pant
"""
from string import punctuation
import nltk
#from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
tokenizer=TweetTokenizer()
import re
myre = re.compile(u'['
    u'\U0001F300-\U0001F64F'
    u'\U0001F680-\U0001F6FF'
    u'\u2600-\u26FF\u2700-\u27BF]+', 
    re.UNICODE)
#import enchant

def preprocess(tweet):
    #words=set(nltk.corpus.words.words())
    #stop_words=set(stopwords.words('english'))
    tweet=myre.sub('', tweet)
    tokens=tokenizer.tokenize(tweet)
    lst=[]
    #d=enchant.Dict("en_GB")
    #english=list(filter(lambda t:(d.check(t.lower())) and (t.lower() not in stop_words) and (t not in punctuation),tokens))
    #non_e=list(filter(lambda t:(not d.check(t.lower())) or (t.lower() in stop_words) or (t in punctuation),tokens))
    #english=[]
    #non_e=[]
    if tokens[0]=="RT":
        return lst
    for t in tokens:
        t=t.lower()
        if t[0]=="@":
            t="HANDLE"
        if re.match(r'[a-zA-Z]+',t):
            if (t not in punctuation):# and (t not in stop_words):
            
                if t[0]!="#":
                    if "https" not in t:
                        if "http" not in t:
                            if t.isalpha():
                                lst.append(t)
            
    return lst
            
                
        
"""            if (d.check(t)) :
                english.append(t)
            else:
                non_e.append(t)"""
                    
    #[w for w in tokens if ((w not in punctuation) and not(w in stop_words) and (w.lower() in words or not w.isalpha()))]

"""english=[]
non_e=[]
english,non_e=preprocess(tweet)
print(english)
print(non_e)"""

"""
#__main__
input_path='/home/pant/Desktop/testing_preprocess/try1/rawtext.txt'
fin=open(input_path,"r")
out_path='/home/pant/Desktop/testing_preprocess/try1/rawtext1.txt'
fp=open(out_path,"w")
whole=fin.read()
lwrite=[]
lout=[]
tweets=whole.split("\n")
length=len(tweets)
print(tweets[0])
for i in range(1,length):

    lout=preprocess(tweets[i])
    if lout!=[]:
        lwrite.append("<s> "+" ".join(lout)+" </s>\n")
fp.writelines(lwrite) 

fin.close()
fp.close()"""
