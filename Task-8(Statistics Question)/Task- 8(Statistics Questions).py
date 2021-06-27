#!/usr/bin/env python
# coding: utf-8

# In[2]:


# question 1
## calculating  the Binomial distribution problem

from math import factorial

def b(n,x,p):
    return factorial(n)//factorial(n-x)//factorial(x) * (p ** x) * (1-p) ** (n-x)

b1,g1 = map(float,input().split())
p = b1/(b1 + g1)
r = b(6,3,p) + b(6,4,p) +b(6,5,p) +b(6,6,p)
print("%.3f" % r)


# In[3]:


#question2
# Calculating the binomial distribution problem II
import math 
P = 0.12  #12%  of the pistons they manufacture 
A1 = 0 #first round

for i in range(0, 3):
    A1 += math.factorial(10)/math.factorial(i)/math.factorial(10-i) * P**i * (1-P)**(10-i)
    if i == 1:
        A2 = 1 - A1 #second round 
#print each round upto a scale of 3 decimal places
print(round(A1, 3))
print(round(A2, 3))


# In[5]:


#question3 
## Calculating the Normal disribution problem I
import math 

mean,std = input().split()

cdf = lambda x: 0.5 * (1 + math.erf((x - mean)/(std*(2**0.5))))

# less than 19.5

print('{:.3f}'.format(cdf(input())))

# between 20 and 22

print('{:.3f}'.format((cdf(input())-cdf(input()))))


# In[6]:


#question4
## Calculating the Normal distribution problem II

import math

mean,std = 70,10

cdf = lambda x: 0.5 * (1+math.erf((x-mean)/(std*(2**0.5))))

## Grade greater then 80
print('probability of grade greater then 80 is: {:.2f}'.format((1-cdf(80))*100))

## Grade greater then or equal to 60.(>=60)

print('probability of grade greater then or equal to 60 is: {:.2f}'.format((1-cdf(60))*100))

# grade less then 60 
print('probability of grade less then 60 is: {:.2f}'.format(cdf(60)*100))


# In[7]:


#question 5
#central limit theorem I
import math

H = int(input())
B = int(input())
C = int(input())
INPUT = math.sqrt(B) * int(input())

print(round(0.5 * (1 + math.erf((H - (B * C)) / (INPUT * math.sqrt(2)))), 4))


# In[8]:


#question 6

#Central Limit theorem II
import math

TICKETS = 250
STUDENTS = 100
MEAN = 2.4
SD = 2

MU = STUDENTS * MEAN
S = math.sqrt(100)*SD

def normal_distribution(x, mu, sd):
    '''Function to calculate the distribution'''
    return 1/2*(1+math.erf((x-mu)/(sd*math.sqrt(2))))

print(round(normal_distribution(x=TICKETS, mu=MU, sd=S), 4))


# In[9]:


#question7
## Calculating the central limit theorem problem 3

from math import sqrt

s = int(input())
mean = int(input())
std = int(input())
interval = float(input())
z = float(input())

print(round(mean-(std/sqrt(s))*z,2))
print(round(mean+(std/sqrt(s))*z,2)


# In[10]:


#quetion 7
#Pearson Correlation Coefficient I


def std(x):
    return (sum([(i-(sum(x))/len(x))**2 for i in x])/len(x))**0.5

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

X_M = sum(X)/len(X)
Y_M = sum(Y)/len(Y)

X_S = std(X)
Y_S = std(Y)

print(round(sum([(i-X_M)*(j-Y_M) for i, j in zip(X, Y)])/(N*X_S*Y_S), 3))


# In[12]:


#question 8
#Least Square Regression Line
def mean(X):
    '''To calculate the mean'''
    return sum(X)/len(X)

def lsr(X, Y):
    '''To calculate the Least Square Regression'''
    B = sum([(X[i] - mean(X)) * (Y[i] - mean(Y)) for i in range(len(X))])/sum([(j - mean(X))**2 for j in X])
    A = mean(Y) - (B*mean(X))
    return A+(B*80)

X = []
Y = []

for i in range(5):
    A, B = list(map(int, input().split()))
    X.append(A)
    Y.append(B)

print(round(lsr(X, Y), 3))


# In[ ]:


#question-9
##multiple linear regression
from sklearn import linear_model

M, N = list(map(int, input().strip().split()))
X = [0]*N
Y = [0]*N

for i in range(N):
    inp = list(map(float, input().strip().split()))
    X[i] = inp[:-1]
    Y[i] = inp[-1]

LM = linear_model.LinearRegression()
LM.fit(X, Y)
A = LM.intercept_
B = LM.coef_

Q = int(input())

for i in range(Q):
    f = list(map(float, input().strip().split()))
    Y = A + sum([B[j] * f[j] for j in range(M)])
    print(round(Y, 2))


# In[ ]:




