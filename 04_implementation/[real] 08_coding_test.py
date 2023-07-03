# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#문자열 재정렬

import string
import numpy as np
import random


letter_len = np.random.randint(1, 10000)

string_pool = string.ascii_uppercase + string.digits
letters = ''
for i in range(letter_len):
    letters += random.choice(string_pool)

let = ''
nums = 0

for i in range(letter_len):
    try:
        if type(int(letters[i])) == int:
            nums += int(letters[i])
    
    except:
        let += letters[i]

sorted_letter = ''.join(sorted(let))

print(sorted_letter + str(nums))
















            
            
