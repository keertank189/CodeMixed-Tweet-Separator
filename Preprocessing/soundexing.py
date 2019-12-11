#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:29:23 2017

@author: pant
"""

import soundextry1
s=soundextry1.getSoundex

en_nons_path="/home/pant/Desktop/english/train_data/"
en_nons_files=["eng_huge_set_clean.txt"]
#en_nons_files=["english.clean","english_clean_my.txt"]
#create new list for new files to append
hi_nons_path="/home/pant/Desktop/hindi/train_data/"
#hi_nons_files=["hindi.clean.random"]
hi_nons_files=["hin_huge_training_data.txt"]

test_file_path="/home/keertan/Documents/CDSAML/news/"
test_files=["twitter_data_pure_mixed.txt"]
#test_files=["queries_from_training_data.txt"]
"""for en_nons_file in en_nons_files:
    
    point=open(en_nons_path+en_nons_file,"r")
    s8=open(en_nons_path+"s8_"+en_nons_file,"w")
    x=point.readlines()
    num_s=len(x)
    for tw in range(num_s):
        x[tw]=x[tw].split()
        wc=len(x[tw])
        for i in range(1,wc-1):
            x[tw][i]=s(x[tw][i],8)
        x[tw]=" ".join(x[tw])+"\n"
    
    s8.writelines(x)   
point.close()
s8.close()"""
for test_file in test_files:
    
    point=open(test_file_path+test_file,"r")
    s8=open(test_file_path+"s8_"+test_file,"w")
    x=point.readlines()
    num_s=len(x)
    for tw in range(num_s):
        x[tw]=x[tw].split()
        wc=len(x[tw])
        for i in range(1,wc-1):
            x[tw][i]=s(x[tw][i],8)
        x[tw]=" ".join(x[tw])+"\n"
    
    s8.writelines(x)   
point.close()
s8.close()
"""for hi_nons_file in hi_nons_files:
    
    point=open(hi_nons_path+hi_nons_file,"r")
    s8=open(hi_nons_path+"s8_"+hi_nons_file,"w")
    x=point.readlines()
    num_s=len(x)
    for tw in range(num_s):
        x[tw]=x[tw].split()
        wc=len(x[tw])
        for i in range(1,wc-1):
            x[tw][i]=s(x[tw][i],8)
        x[tw]=" ".join(x[tw])+"\n"
    
    s8.writelines(x)   
point.close()
s8.close()"""