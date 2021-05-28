#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Task3 Programming
#question1
#polar coordinates
import cmath 
a =  complex(input().strip())
A =  cmath.polar(a)
print(A[0])
print(A[1])


# ### 

# In[2]:


#question 2
#Find MBC ANGLE
import math
ab=int(input())
bc=int(input())
theta=math.atan(ab/bc)
deg=round(math.degrees(theta))
print(deg,chr(176),sep='' ) 


# In[1]:


#question3
#triangle quest2
for n in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**n-1)//9)**2) 


# In[2]:


#question 4
#mod divmod
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input()) 
print(int (a/b))
print(int(a%b))
print(divmod(a,b))


# In[1]:


#question5
#power mod m
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))#print a^b
print(pow(a,b,m))#print a^b mod m


# In[2]:


#question 6
#integers comes ranges
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print((pow(a,b)+pow(c,d)) )


# In[3]:


#question7
#triangle quest 2
for n in range(1,int(input())): 
    print(((10**n)//9)*n)


# In[ ]:




