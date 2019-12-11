#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:02:37 2017

@author: pant
"""

def getSoundex(test,n):
    test=improve(test)
    final=" "
    i=0
    code=' '
    for ch in test:
        if(i==0):
            final=ch
            i+=1
        else:
            code=str(getsoundexdigit(ch))
            if code!=final[len(final)-1]:
                final+=code
    final=removeplaceholders(final)
    final=fixlen(final,n)
    return final
def getsoundexdigit(ch):
    if ch in "BFPV":
        return 1
    elif ch in "CGJKQSXZ":
        return 2
    elif ch in "DT":
        return 3
    elif ch in "L":
        return 4
    elif ch in "MN":
        return 5
    elif ch in "R":
        return 6
    else:
        return " "

def removeplaceholders(sub): 
    sub=sub.replace(" ",'')
    return sub

def fixlen(final,n):
    l=len(final)
    if l<n:
        final+=('0'*(n-l))
    elif l>n:
       final=final[:n-1]
    return final

def improve(test):
    test=test.upper()
    anywhere=[['DG','G'],['GN','N'],['KN','N'],['PH','F'],['MB','M'],['TCH','CH']]
    begin=[['PF','F'],['PS','S']]
    not_begin=[['GH','H']]
    #our own
    own=[['SCE','S'],['SCI','SI']]
    for i in begin:
        if test[:2]==i[0]:
            test=i[1]+test[2:]
    for i in not_begin:
        if i[0] in test[1:]:
            test=test.replace(i[0],i[1])
            
    for i in anywhere:
        if i[0] in test:
            test=test.replace(i[0],i[1])
    for i in own:
        if i[0] in test:
            test=test.replace(i[0],i[1])
        
    return test

print(getSoundex("Sab",5))