#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:03:02 2017

@author: keertan krishnan
"""
import json
from preprocess import preprocess
tweets_data_path = '/home/keertan/Documents/CDSAML/CDSAML Preprocessing Code/twitter_data_try1_hindi.txt'
tweets_out_path='/home/keertan/Documents/CDSAML/CDSAML Preprocessing Code/twitter_data_clean_try1_hindi.txt'
finput=open(tweets_data_path,"r")
fout=open(tweets_out_path,'w')
tweets_data=[]
for line in finput:
    try:
        tweet = json.loads(line)
        if tweet["lang"] in ["hi","und"]:
            tout=tweet["text"].split(" ")
            ttout=[]
            if tout[0]=="RT":
                tout=""
            for t in tout:
                t=t.lower()
                if t[0]=="@":
                    t="HANDLE"
                if re.match(r'[a-zA-Z]+',t):
                    if (t not in punctuation):# and (t not in stop_words):
            
                        if t[0]!="#":
                            if "https" not in t:
                                if "http" not in t:
                                    if t.isalpha():
                                        ttout.append(t)
            ttout=(" ").join(ttout)
            tweets_data.append(ttout)
            fout.write(ttout)
            
            """lout=preprocess(tweet["text"])
            if lout!=[]:
                lout="<s> "+" ".join(lout)+" </s>\n"
                tweets_data.append(lout)
                fout.write(lout)"""
        #print(tweet['text'])
    except:
        continue


finput.close()
fout.close()

