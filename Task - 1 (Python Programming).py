#!/usr/bin/env python
# coding: utf-8

# In[6]:


# question 1

print("Hello,World")


# In[11]:


#question 2
#arithmetic operators
a=3
b=2
print(int(a+b))
print(int(a-b))
print(int(a*b))


# In[12]:


#question 3
#division
a = 4
b = 3
print(a//b)
print(a/b)


# In[2]:


#question4 
#using if else n is even or odd ,if n is even and in range 2-5 then print "not weird" and less than 6-20 print weird or greater than 20 print " not weird" that 
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    A= n%2
    if A!=0:
        print('Weird')
    elif A==0 and n in range(2,5):
        print('Not Weird')
    elif A==0 and n in range(6,20):
        print('Weird')
    elif A==0 and n>20:
        print('Not Weird')


# In[3]:


#question 5 loops
if __name__ == '__main__':
    n = int(input())
    for j in range (0,n):
        print(j*j)        


# In[1]:


#question 6 functions
def is_leap(year):
    if year % 4 == 0 : return True
    else: return False
    if year % 100 == 0 : return False
    else:return true
    if year% 400 ==0: 
        return False 
        return leap 
year = int(input())
print(is_leap(year))


# In[10]:


#question 7
if __name__ == '__main__' : 
      n = int(input())    
for a in range(1,n+1):
     print(a,end="")


# In[ ]:




