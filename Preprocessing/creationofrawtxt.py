#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:03:02 2017

@author: keertan krishnan
"""
import json
from preprocess import preprocess
tweets_data_path = '/Users/keertankrishnan/Documents/Project Work/CDSAML/Old Laptop Files/CDSAML/news/output.txt'
tweets_out_path='/Users/keertankrishnan/Documents/Project Work/CDSAML/Old Laptop Files/CDSAML/news/optext.txt'
finput=open(tweets_data_path,"r")
fout=open(tweets_out_path,'w')
tweets_data=[]
for line in finput:
    try:
        tweet = json.loads(line)
        if tweet["lang"] in ["hi","und"]:
            #tout=tweet["text"].split(" ")
            lout=preprocess(tweet["text"])
            if lout!=[]:
                lout="<s> "+" ".join(lout)+" </s>\n"
                tweets_data.append(lout)
                fout.write(lout)
        #print(tweet['text'])
    except:
        continue


finput.close()
fout.close()

