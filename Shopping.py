# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
i=0
a=0
b=0

while i < 3:
    n = random.random()
    num = int(n*10)  
    print(num)
    i = i + 1
    if (num % 2) == 0:  
       print("Yes!!".format(num))  
       a= a+1
    else:  
       print("NO Sorry".format(num))
       b = b+1

if a>b:
    print("yes no worries ;)))")
    
else:
    print("God bless you my son")