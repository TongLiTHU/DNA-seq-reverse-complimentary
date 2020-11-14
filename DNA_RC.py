# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:12:49 2020

@author: TONG
"""

#!/usr/bin/python3
#generate reverse complimentary sequence from sequence.txt and perform bases statistics
with open('sequence.txt','r',encoding='utf-8') as f:
  sequence = f.read()
sequence = sequence.upper()
a='A'; t='T'; c='C'; g='G'
print("Original DNA sequence is：",sequence,'\n')

str = "Statistics of original DNA sequence"
print (str.center(80, '*'))
print ("Length: ", sequence.count(a)+sequence.count(t)+sequence.count(c)+sequence.count(g),'bp')
print ("Number of 'A' base: ", sequence.count(a))
print ("Number of 'T' base: ", sequence.count(t))
print ("Number of 'C' base: ", sequence.count(c))
print ("Number of 'G' base: ", sequence.count(g))
print ("Number of 'A+T' bases: ", sequence.count(a)+sequence.count(t))
print ("Number of 'C+G' bases: ", sequence.count(c)+sequence.count(g))
print ("CG content: ", round((sequence.count(c)+sequence.count(g))/len(sequence)*100,2),'%') 
print ("AT content: ", round((sequence.count(a)+sequence.count(t))/len(sequence)*100,2),'%') 
print('\n')
sequence = sequence[::-1] #generating reverse seuqence

intab = "ATCG"
outtab = "TAGC"
trantab = str.maketrans(intab, outtab) #defining base pairing rules

sequence = sequence.translate(trantab) #generating reverse complimentary sequence
print ("Reverse complimentary DNA sequence is:", sequence,'\n')

str = "Statistics of reverse complimentary DNA sequence"
print (str.center(80, '*'))
print ("Length: ", sequence.count(a)+sequence.count(t)+sequence.count(c)+sequence.count(g),'bp')
print ("Number of 'A' base: ", sequence.count(a))
print ("Number of 'T' base: ", sequence.count(t))
print ("Number of 'C' base: ", sequence.count(c))
print ("Number of 'G' base: ", sequence.count(g))
print ("Number of 'A+T' bases: ", sequence.count(a)+sequence.count(t))
print ("Number of 'C+G' bases: ", sequence.count(c)+sequence.count(g))
print ("CG content: ", round((sequence.count(c)+sequence.count(g))/len(sequence)*100,2),'%') 
print ("AT content: ", round((sequence.count(a)+sequence.count(t))/len(sequence)*100,2),'%') 

