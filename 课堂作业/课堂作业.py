# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:07:16 2022

@author: Surface
"""

fin=open("C:\words.txt‪")
line=fin.readline()
word=line.strip()

for line in fin:
    word=line.strip()
    if len(word)>20:
        print(word)
        
def has_no_e(word):
    for letter in word:
        if letter=="e":
            return False
        return True
    
fin=open("C:\words.txt‪") 
count=0  
    
    
    
for line in fin:
    word=line.strip()
    if has_no_e==True:
        count=count+1
print(word)
        
    
    
    
def avoids(word,forbidden_letters):
    for letter in word:
        if letter in forbidden_letters:
            return False
        return True

fin=open("C:\words.txt‪") 
count=0




for line in fin:
    count=0
    word=line.strip()
    if avoids==True:
        count=count+1
print(count)