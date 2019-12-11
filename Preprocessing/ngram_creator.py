#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:04:07 2017

@author: pant
"""

def ngrams(input, n):
  input = input.split(' ')
  output = {}
  for i in range(len(input)-n+1):
    g = ' '.join(input[i:i+n])
    output.setdefault(g, 0)
    output[g] += 1
  return output

hi_in_dir='/home/pant/Desktop/hindi/train_data/'
#hi_files=["s8_hindi.clean.random"]
hi_files=["s8_hin_huge_training_data.txt"]

#make new list if you wish to add more n grams to existing files
en_in_dir='/home/pant/Desktop/english/train_data/'
en_files=["s8_eng_huge_set_clean.txt"]
#en_files=["s8_english.clean","s8_english_clean_my.txt"]
for i in range(1,5):
    for en_file in en_files:
        
        finput=open(en_in_dir+en_file,"r")
        ngram=open(en_in_dir+"/ngrams/"+"s8_en_"+str(i)+"gram.txt","a")
        x=finput.readlines()
        text=''
        for k in x:
            k=k.rstrip()
            text+=k
        
        dictionary=ngrams(text,i)
        for k in dictionary:
            ngram.write(k+" "+str(dictionary[k])+"\n")
        finput.close()
    ngram.close()
    for hi_file in hi_files:
        
        finput=open(hi_in_dir+hi_file,"r")
        ngram=open(hi_in_dir+"/ngrams/"+"s8_hi_"+str(i)+"gram.txt","a")
        #ngram=open(hi_in_dir+"/ngrams/"+"hi_"+str('1')+"gram.txt","w")
        x=finput.readlines()
        text=''
        for k in x:
            k=k.rstrip()
            text+=k
        
        dictionary=ngrams(text,i)
        #dictionary=ngrams(text,1)
        for k in dictionary:
            ngram.write(k+" "+str(dictionary[k])+"\n")
        finput.close()
    ngram.close()
    
