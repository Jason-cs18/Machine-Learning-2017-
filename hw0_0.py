#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:07:26 2018

@author: apple
"""

import numpy as np
from collections import Counter


# homework 0
txt_data = open('words.txt')

txt_data = txt_data.read()[:len(txt_data.read())-1]

# split data
txt_data = txt_data.split(' ')

unique_word = np.unique(txt_data)

unique_word_dict = {}
unique_word_dict_1 = {}

for i in range(len(unique_word)):
    unique_word_dict[unique_word[i]] = i
    unique_word_dict_1[i] = unique_word[i]
                    
for i in range(len(txt_data)):
    txt_data[i] = unique_word_dict[txt_data[i]]
    
res = dict(Counter(txt_data))
res_0 = []
for key, value in res.items():
    res_0.append((unique_word_dict_1[key], key, value))

# res_0 for hw_0_wordtxt
print(res_0)


    
    





