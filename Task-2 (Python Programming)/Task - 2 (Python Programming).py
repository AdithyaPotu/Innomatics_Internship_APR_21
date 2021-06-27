#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 8
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())   
print([[i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if (i+j+k) != n])


# In[17]:


#question num 9 
#find the runner up score :
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = max(arr)
    i=0
    while(i<n):
        if result ==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))


# In[1]:


# question 10 
#nested lists
if __name__ == '__main__':

    grade_lst = []

    marksheet = []

    for _ in range(int(input())):

        name = input()

        grade = float(input())

        marksheet.append([name,grade])

        grade_lst.append(grade)

    second_lowest = sorted(list(set(grade_lst)))[1]

    names = [name for name,marks in sorted(marksheet) if marks == second_lowest]

    print('\n'.join(names))


# In[7]:


#question11
#find the percentage
if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
query_name = input()
mark = student_marks[query_name]
print("{0:.2f}".format(sum (mark) /(len(scores)))) 


# In[1]:


#question12
#Lists
if __name__ == '__main__':
        N = int(input())
        arr = []
        for t in range(N):
            args = input().strip().split(" ")
            if args[0] == "append":
                arr.append(int(args[1]))
            elif args[0] == "insert":
                arr.insert(int(args[1]), int(args[2]))
            elif args[0] == "remove":
                arr.remove(int(args[1]))
            elif args[0] == "pop":
                arr.pop()
            elif args[0] == "sort":
                arr.sort()
            elif args[0] == "reverse":
                arr.reverse()
            elif args[0] == "print":
                print (arr)


# In[2]:


#question 13
# tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    K = tuple(integer_list)
    print (hash(K));


# In[3]:


#question14
#sets
def average(array):
    s = set(array)
    avg = sum(s) / len(s)
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[1]:


#question15
#NO IDEA
n,m = input().split()

arr = input().split()

A = set(input().split()) 
B = set(input().split())
print (sum([(i in A) - (i in B) for i in arr]) )


# In[13]:


#question16
#symmetric set
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__': 
    N=int(input())
    a=set(map(int,input().split()))
    M=int(input())
    b=set(map(int,input().split()))
for i in sorted(a.union(b)):
    if i not in a.intersection(b):
        print (i)  


# In[1]:


#question 17
# set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
stamp = set()
for i in range(n) :
      stamp.add(input())
print (len(stamp))


# In[2]:


#question 18
#set.remove(),pop(),discard()
n = int(input())
s = set(map(int, input().split()))
a = int(input())
for i in range(a):
    s1=list(input().split())
    if s1[0]=="pop":
        s.pop()
    elif s1[0]=="remove":
        s.remove(int(s1[1]))
    elif s1[0]=="discard":
        s.discard(int(s1[1]))
sum=0
for i in s:
    sum = sum+i
print(sum)


# In[3]:


#question 19
#Calculate the Union in between two given sets and find number of students in Class
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
ans = a.union(b)
count = 0
for i in ans:
    count += 1
print(count)


# In[ ]:


#question 20
#Find the Intersection in between the two sets
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b= set(map(int,input().split()))
ans = a.intersection(b)
count = 0
for i in ans:
    count += 1
print(count)


# In[ ]:


#question21
#Set .difference() Operation


## Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
ans = a.difference(b)
count = 0
for i in ans:
    count += 1
print(count)


# In[ ]:


#question22
#Find the Symmentric Difference Between two sets
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
ans = a.symmetric_difference(b)
count = 0
for i in ans:
    count += 1
print(count)


# In[ ]:


#questiom23
#Find the Set Mutations on the given input data
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = set(map(int,input().split()))
for i in range (int(input())):
    c=input().split()
    s=set(map(int,input().split()))
    if c[0]=='intersection_update':
        m&=s
    elif c[0]=='update':
        m|=s
    elif c[0]=='difference_update':
        m-=s
    elif c[0]=='symmetric_difference_update':
        m^=s
print(sum(m))


# In[ ]:


#question24
#Finding captian room in given list of input data
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=map(int,input().split(" "))
a=sorted(a)
for i in range(1,len(a)):
    if i!=len(a)-1:
        if a[i]!=a[i-1] and a[i]!=a[i+1]:
            print (a[i])
            break
    else:
        print (a[i])


# In[ ]:


#question25
#check subsets
# Enter your code here. Read input from STDIN. Print output to STDOUT
def checker():
    x =int(input())
    a = set(map(int,input().split()))
    y = int(input())
    b = set(map(int,input().split()))
 
    l = []
    for i in a:
        if i in b:
            l.append(i)
    l = set(l)
    if l == a:
        print(True)
    else:
        print(False)
        
t = int(input())
for i in range(t):
    checker()


# In[ ]:


#question 26
#Finding the Strict Superset in a given sets
A = set(map(int, input().split()))
for i in range(int(input())):
    N = set(map(int, input().split()))
    if A.issuperset(N) != True or len(A) == len(N): 
        print(False)
        break 
else: print(True)


# In[ ]:




