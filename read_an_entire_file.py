# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:03:16 2020

@author: SATHWIK
"""


  
a=str(input('enter the name of the file with .txt extension'))
file=open(a,"r")
line=file.readline()
while (line!=""):
    print(line)
    line=file.readline()
file.close()