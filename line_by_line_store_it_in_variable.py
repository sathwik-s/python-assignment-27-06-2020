# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:01:36 2020

@author: SATHWIK
"""


def file_name(fname):
    with open(fname,"r") as myfile:
        data=myfile.readlines()
        print(data)
file_read('file.txt')