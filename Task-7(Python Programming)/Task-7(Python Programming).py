#!/usr/bin/env python
# coding: utf-8

# # Descriptive statistics
# 

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[10]:


df = pd.read_csv('F:\Innomatics_Internship_APR_21\data.csv')


# In[11]:


df.head()


# In[12]:


#checking number of rows and columns
df.shape


# In[13]:


df.columns


# In[14]:


df.describe(include="all")


# # 1. Let's have a look on significace of the Mean
# Mean is the one of the Measure of central tendency it can be calculated by adding the sum of all data points to the given number of data points.
# 
# Mean is the most common measure of central tendency but it has a huge downside because it is easily effected by outliers where value is significantly greater than other values in the data set.
# 
# Following is the formula used for calculating the Mean 

# $Exi$/N

# # Calculating the Mean without using library function

# In[15]:


# lets create some temporary data to find mean

num = [10,15,20,30,40,50]
n = len(num)
  
gsum = sum(num)
mean = gsum / n
  
print("Mean of the given data is: " + str(mean))


# Lets calculate the Mean from given data

# # calculating mean from given data

# In[16]:


df.mean()


# # 2. Let us have a look on Median and its significance
# Median is the middle value of a sorted data set; found by ordering all data points and picking out the one in the middle (or if there are two middle numbers, taking the mean of those two numbers).
# The median is sometimes used as opposed to the mean when there are outliers in the sequence that might skew the average of the values. The median of a sequence can be less affected by outliers than the mean.¶
# To caluculate the Median from the given data we use following formula
# $$Mm = l + \frac{\frac{1}{2}- cf}{f} \cdot h$$

# Let's Calculate the median from given data using inbuilt median function

# In[17]:


# Calculating the median in the given dataset

df.median()


# let's calculate median without using inbuilt function with a example

# In[18]:


# list of elements to calculate median
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()
  
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))


# # 3. Lets have a look on Mode and its functionality with a example
# The mode is the number that occurs most often within a set of numbers in the data, A set of data may have one mode, more than one mode, or no mode at all.
# Mode is most useful as a measure of central tendency when examining categorical data, such as models of cars or flavors of soda, for which a mathematical average median value based on ordering can not be calculated.¶

# ![download.png](attachment:download.png)

# Lets calculate the mode from the given data using inbuilt function

# In[21]:


df.mode()


# Lets calculate the mode without using the inbuilt function with a example

# In[23]:


from collections import Counter
  
# list of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "the mode from n_num is : " + ', '.join(map(str, mode))
      
print(get_mode)


# # 4. Let us discuss about the Variance and its functioning
# The term Variance refers to a statistical measurement of the spread between numbers in a data set. More specifically, variance measures how far each number in the set is from the mean and thus from every other number in the set. Variance is often depicted by this symbol: $\sigma^2$
# In statistics, variance measures variability from the average or mean. It is calculated by taking the differences between each number in the data set and the mean, then squaring the differences to make them positive, and finally dividing the sum of the squares by the number of values in the data set.
# Let's have a look on formula of Variance
# $$\sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \mu)^2} {n}$$

# <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="93.117979pt" height="21.955572pt" viewBox="0 0 93.117979 21.955572" version="1.1">
# <defs>
# <g>
# <symbol overflow="visible" id="glyph0-0">
# <path style="stroke:none;" d="M 6.375 -5.140625 L 4.046875 -5.140625 C 1.78125 -5.140625 0.328125 -3.1875 0.328125 -1.5625 C 0.328125 -0.515625 0.953125 0.125 2.078125 0.125 C 3.75 0.125 5.265625 -1.28125 5.265625 -2.609375 C 5.265625 -3.5 4.59375 -3.484375 4.109375 -4.25 L 6.15625 -4.25 Z M 4.265625 -2.65625 C 4.265625 -1.6875 3.421875 -0.125 2.265625 -0.125 C 1.703125 -0.125 1.328125 -0.484375 1.328125 -1.203125 C 1.328125 -2.890625 2.734375 -4.25 3.5625 -4.25 C 3.953125 -4.015625 4.265625 -3.421875 4.265625 -2.65625 Z M 4.265625 -2.65625 "/>
# </symbol>
# <symbol overflow="visible" id="glyph1-0">
# <path style="stroke:none;" d="M 4.03125 -1.171875 L 3.921875 -1.21875 C 3.640625 -0.734375 3.453125 -0.640625 3.09375 -0.640625 L 1.109375 -0.640625 L 2.515625 -2.140625 C 3.265625 -2.953125 3.609375 -3.578125 3.609375 -4.25 C 3.609375 -5.09375 2.984375 -5.75 2.03125 -5.75 C 0.984375 -5.75 0.4375 -5.0625 0.25 -4.0625 L 0.4375 -4.015625 C 0.78125 -4.859375 1.078125 -5.125 1.6875 -5.125 C 2.40625 -5.125 2.875 -4.703125 2.875 -3.921875 C 2.875 -3.203125 2.5625 -2.546875 1.765625 -1.71875 L 0.25 -0.109375 L 0.25 0 L 3.578125 0 Z M 4.03125 -1.171875 "/>
# </symbol>
# <symbol overflow="visible" id="glyph1-1">
# <path style="stroke:none;" d="M 5.28125 -1.875 L 5.28125 -2.4375 L 0.546875 -2.4375 L 0.546875 -1.875 Z M 5.28125 -1.875 "/>
# </symbol>
# <symbol overflow="visible" id="glyph2-0">
# <path style="stroke:none;" d="M 7.640625 -3.84375 L 7.640625 -4.625 L 0.578125 -4.625 L 0.578125 -3.84375 Z M 7.640625 -1.4375 L 7.640625 -2.234375 L 0.578125 -2.234375 L 0.578125 -1.4375 Z M 7.640625 -1.4375 "/>
# </symbol>
# <symbol overflow="visible" id="glyph3-0">
# <path style="stroke:none;" d="M 0.390625 8.515625 C 0.359375 8.515625 0.34375 8.488281 0.34375 8.4375 C 0.34375 8.425781 0.347656 8.414062 0.359375 8.40625 L 3.546875 4.65625 L 0.359375 0.265625 C 0.347656 0.253906 0.34375 0.242188 0.34375 0.234375 L 0.34375 0.046875 C 0.34375 0.0351562 0.347656 0.0234375 0.359375 0.015625 C 0.367188 0.00390625 0.378906 0 0.390625 0 L 7.640625 0 L 8.359375 1.703125 L 8.1875 1.703125 C 8 1.273438 7.6875 0.957031 7.25 0.75 C 6.8125 0.539062 6.351562 0.410156 5.875 0.359375 C 5.40625 0.316406 4.851562 0.296875 4.21875 0.296875 L 1.4375 0.296875 L 4.28125 4.21875 C 4.289062 4.226562 4.296875 4.238281 4.296875 4.25 C 4.296875 4.269531 4.289062 4.285156 4.28125 4.296875 L 1.15625 7.96875 L 4.28125 7.96875 C 4.894531 7.96875 5.441406 7.941406 5.921875 7.890625 C 6.398438 7.847656 6.851562 7.722656 7.28125 7.515625 C 7.71875 7.304688 8.019531 6.984375 8.1875 6.546875 L 8.359375 6.546875 L 7.640625 8.515625 Z M 0.390625 8.515625 "/>
# </symbol>
# <symbol overflow="visible" id="glyph4-0">
# <path style="stroke:none;" d="M 2.109375 -4.796875 C 2.109375 -5.03125 1.921875 -5.234375 1.71875 -5.234375 C 1.5 -5.234375 1.34375 -5.0625 1.34375 -4.8125 C 1.34375 -4.546875 1.484375 -4.390625 1.71875 -4.390625 C 1.921875 -4.390625 2.109375 -4.5625 2.109375 -4.796875 Z M 1.78125 -0.90625 C 1.4375 -0.453125 1.234375 -0.28125 1.109375 -0.28125 C 1.046875 -0.28125 0.984375 -0.328125 0.984375 -0.40625 C 0.984375 -0.515625 1.03125 -0.625 1.078125 -0.765625 L 1.828125 -3.5 L 1.796875 -3.53125 C 0.984375 -3.375 0.828125 -3.359375 0.515625 -3.328125 L 0.515625 -3.203125 C 0.9375 -3.1875 1.03125 -3.171875 1.03125 -3.015625 C 1.03125 -2.9375 0.984375 -2.796875 0.953125 -2.65625 L 0.5625 -1.234375 C 0.453125 -0.796875 0.390625 -0.515625 0.390625 -0.359375 C 0.390625 -0.0625 0.515625 0.09375 0.78125 0.09375 C 1.1875 0.09375 1.4375 -0.15625 1.875 -0.828125 Z M 1.78125 -0.90625 "/>
# </symbol>
# <symbol overflow="visible" id="glyph4-1">
# <path style="stroke:none;" d="M 3.6875 -0.9375 C 3.625 -0.859375 3.5625 -0.796875 3.515625 -0.734375 C 3.28125 -0.4375 3.140625 -0.296875 3.03125 -0.296875 C 2.921875 -0.296875 2.890625 -0.375 2.890625 -0.453125 C 2.890625 -0.515625 2.921875 -0.640625 3.015625 -0.9375 L 3.453125 -2.5625 C 3.5 -2.734375 3.53125 -2.890625 3.53125 -3.046875 C 3.53125 -3.328125 3.359375 -3.53125 3.015625 -3.53125 C 2.5 -3.53125 1.96875 -3.046875 1.171875 -1.765625 L 1.703125 -3.515625 L 1.671875 -3.53125 C 1.25 -3.4375 1.03125 -3.40625 0.375 -3.28125 L 0.375 -3.15625 C 0.78125 -3.140625 0.890625 -3.09375 0.890625 -2.9375 C 0.890625 -2.890625 0.890625 -2.84375 0.875 -2.796875 L 0.109375 0 L 0.71875 0 C 1.09375 -1.265625 1.15625 -1.453125 1.515625 -1.984375 C 2.015625 -2.734375 2.375 -3.125 2.703125 -3.125 C 2.8125 -3.125 2.890625 -3.03125 2.890625 -2.890625 C 2.890625 -2.796875 2.84375 -2.5 2.78125 -2.25 L 2.421875 -0.953125 C 2.3125 -0.546875 2.296875 -0.4375 2.296875 -0.359375 C 2.296875 -0.0625 2.46875 0.078125 2.671875 0.078125 C 3.046875 0.078125 3.25 -0.09375 3.796875 -0.828125 Z M 3.6875 -0.9375 "/>
# </symbol>
# <symbol overflow="visible" id="glyph5-0">
# <path style="stroke:none;" d="M 5.09375 -2.5625 L 5.09375 -3.09375 L 0.390625 -3.09375 L 0.390625 -2.5625 Z M 5.09375 -0.953125 L 5.09375 -1.484375 L 0.390625 -1.484375 L 0.390625 -0.953125 Z M 5.09375 -0.953125 "/>
# </symbol>
# <symbol overflow="visible" id="glyph5-1">
# <path style="stroke:none;" d="M 3.15625 0 L 3.15625 -0.125 C 2.546875 -0.125 2.390625 -0.265625 2.390625 -0.609375 L 2.390625 -5.390625 L 2.3125 -5.40625 L 0.890625 -4.6875 L 0.890625 -4.5625 L 1.109375 -4.640625 C 1.25 -4.703125 1.390625 -4.75 1.46875 -4.75 C 1.625 -4.75 1.703125 -4.625 1.703125 -4.359375 L 1.703125 -0.765625 C 1.703125 -0.3125 1.53125 -0.15625 0.9375 -0.125 L 0.9375 0 Z M 3.15625 0 "/>
# </symbol>
# <symbol overflow="visible" id="glyph5-2">
# <path style="stroke:none;" d="M 3.796875 -1.09375 L 3.6875 -1.140625 C 3.421875 -0.703125 3.25 -0.609375 2.90625 -0.609375 L 1.046875 -0.609375 L 2.359375 -2.015625 C 3.078125 -2.765625 3.390625 -3.375 3.390625 -4 C 3.390625 -4.796875 2.8125 -5.40625 1.90625 -5.40625 C 0.921875 -5.40625 0.40625 -4.75 0.234375 -3.8125 L 0.40625 -3.78125 C 0.734375 -4.5625 1.015625 -4.8125 1.578125 -4.8125 C 2.265625 -4.8125 2.703125 -4.421875 2.703125 -3.6875 C 2.703125 -3.015625 2.40625 -2.40625 1.65625 -1.609375 L 0.234375 -0.09375 L 0.234375 0 L 3.359375 0 Z M 3.796875 -1.09375 "/>
# </symbol>
# <symbol overflow="visible" id="glyph6-0">
# <path style="stroke:none;" d="M 2.96875 8.203125 C 2.34375 7.710938 1.882812 7.09375 1.59375 6.34375 C 1.300781 5.601562 1.15625 4.8125 1.15625 3.96875 C 1.15625 3.125 1.300781 2.328125 1.59375 1.578125 C 1.882812 0.828125 2.34375 0.210938 2.96875 -0.265625 C 2.96875 -0.273438 2.976562 -0.28125 3 -0.28125 L 3.09375 -0.28125 C 3.101562 -0.28125 3.113281 -0.269531 3.125 -0.25 C 3.144531 -0.238281 3.15625 -0.226562 3.15625 -0.21875 C 3.15625 -0.195312 3.148438 -0.179688 3.140625 -0.171875 C 2.867188 0.0859375 2.640625 0.378906 2.453125 0.703125 C 2.265625 1.035156 2.113281 1.375 2 1.71875 C 1.894531 2.070312 1.816406 2.4375 1.765625 2.8125 C 1.722656 3.195312 1.703125 3.585938 1.703125 3.984375 C 1.703125 5.816406 2.179688 7.191406 3.140625 8.109375 C 3.148438 8.117188 3.15625 8.132812 3.15625 8.15625 C 3.15625 8.164062 3.144531 8.175781 3.125 8.1875 C 3.113281 8.207031 3.101562 8.21875 3.09375 8.21875 L 3 8.21875 C 2.976562 8.21875 2.96875 8.210938 2.96875 8.203125 Z M 2.96875 8.203125 "/>
# </symbol>
# <symbol overflow="visible" id="glyph6-1">
# <path style="stroke:none;" d="M 0.375 8.21875 C 0.332031 8.21875 0.3125 8.195312 0.3125 8.15625 C 0.3125 8.132812 0.316406 8.117188 0.328125 8.109375 C 0.691406 7.753906 0.976562 7.351562 1.1875 6.90625 C 1.394531 6.457031 1.539062 5.988281 1.625 5.5 C 1.707031 5.007812 1.75 4.5 1.75 3.96875 C 1.75 2.125 1.273438 0.742188 0.328125 -0.171875 C 0.316406 -0.179688 0.3125 -0.195312 0.3125 -0.21875 C 0.3125 -0.257812 0.332031 -0.28125 0.375 -0.28125 L 0.46875 -0.28125 C 0.476562 -0.28125 0.488281 -0.273438 0.5 -0.265625 C 1.125 0.210938 1.582031 0.828125 1.875 1.578125 C 2.164062 2.328125 2.3125 3.125 2.3125 3.96875 C 2.3125 4.8125 2.164062 5.601562 1.875 6.34375 C 1.582031 7.09375 1.125 7.710938 0.5 8.203125 C 0.488281 8.210938 0.476562 8.21875 0.46875 8.21875 Z M 0.375 8.21875 "/>
# </symbol>
# <symbol overflow="visible" id="glyph7-0">
# <path style="stroke:none;" d="M 2.0625 -3.015625 C 1.953125 -3.609375 1.84375 -3.75 1.640625 -3.75 C 1.4375 -3.75 1.15625 -3.703125 0.640625 -3.515625 L 0.546875 -3.46875 L 0.578125 -3.34375 L 0.71875 -3.375 C 0.890625 -3.421875 0.984375 -3.4375 1.0625 -3.4375 C 1.265625 -3.4375 1.328125 -3.375 1.453125 -2.859375 L 1.6875 -1.8125 L 0.984375 -0.8125 C 0.8125 -0.5625 0.640625 -0.40625 0.546875 -0.40625 C 0.5 -0.40625 0.421875 -0.421875 0.328125 -0.484375 C 0.21875 -0.53125 0.140625 -0.578125 0.0625 -0.578125 C -0.109375 -0.578125 -0.234375 -0.4375 -0.234375 -0.265625 C -0.234375 -0.046875 -0.0625 0.09375 0.203125 0.09375 C 0.453125 0.09375 0.625 0.015625 1 -0.484375 L 1.75 -1.5 L 2 -0.484375 C 2.109375 -0.0625 2.234375 0.09375 2.5 0.09375 C 2.828125 0.09375 3.046875 -0.109375 3.546875 -0.875 L 3.421875 -0.953125 C 3.34375 -0.875 3.3125 -0.8125 3.234375 -0.71875 C 3.046875 -0.453125 2.953125 -0.375 2.828125 -0.375 C 2.71875 -0.375 2.640625 -0.484375 2.578125 -0.71875 L 2.3125 -1.859375 C 2.25 -2.0625 2.234375 -2.1875 2.234375 -2.25 C 2.609375 -2.90625 2.921875 -3.28125 3.078125 -3.28125 C 3.28125 -3.28125 3.359375 -3.140625 3.515625 -3.140625 C 3.6875 -3.140625 3.8125 -3.265625 3.8125 -3.4375 C 3.8125 -3.625 3.65625 -3.75 3.453125 -3.75 C 3.078125 -3.75 2.765625 -3.453125 2.171875 -2.53125 Z M 2.0625 -3.015625 "/>
# </symbol>
# <symbol overflow="visible" id="glyph7-1">
# <path style="stroke:none;" d="M 4 -1 C 3.546875 -0.421875 3.421875 -0.3125 3.28125 -0.3125 C 3.234375 -0.3125 3.1875 -0.359375 3.1875 -0.4375 C 3.1875 -0.515625 3.328125 -0.953125 3.359375 -1.09375 L 4.03125 -3.640625 L 3.375 -3.640625 L 3.09375 -2.609375 C 2.953125 -2.0625 2.015625 -0.46875 1.515625 -0.46875 C 1.28125 -0.46875 1.171875 -0.640625 1.171875 -0.875 C 1.171875 -0.953125 1.1875 -1.03125 1.203125 -1.109375 L 1.84375 -3.640625 L 1.203125 -3.640625 L 0.09375 0.796875 C -0.046875 1.328125 -0.15625 1.578125 -0.28125 1.75 L 0.328125 1.75 C 0.515625 1.53125 0.5625 1.109375 0.890625 -0.15625 C 0.9375 -0.015625 1.03125 0.078125 1.203125 0.078125 C 1.71875 0.078125 2.1875 -0.5 2.921875 -1.828125 L 2.9375 -1.828125 L 2.65625 -0.9375 C 2.59375 -0.734375 2.53125 -0.4375 2.53125 -0.296875 C 2.53125 -0.046875 2.703125 0.09375 2.953125 0.09375 C 3.328125 0.09375 3.578125 -0.109375 4.109375 -0.921875 Z M 4 -1 "/>
# </symbol>
# <symbol overflow="visible" id="glyph7-2">
# <path style="stroke:none;" d="M 3.921875 -1 C 3.859375 -0.921875 3.796875 -0.84375 3.734375 -0.78125 C 3.484375 -0.453125 3.34375 -0.328125 3.21875 -0.328125 C 3.109375 -0.328125 3.078125 -0.40625 3.078125 -0.484375 C 3.078125 -0.546875 3.109375 -0.6875 3.203125 -1 L 3.671875 -2.71875 C 3.734375 -2.90625 3.765625 -3.078125 3.765625 -3.234375 C 3.765625 -3.546875 3.578125 -3.75 3.203125 -3.75 C 2.671875 -3.75 2.09375 -3.25 1.25 -1.875 L 1.8125 -3.734375 L 1.78125 -3.75 C 1.328125 -3.65625 1.09375 -3.625 0.40625 -3.484375 L 0.40625 -3.359375 C 0.828125 -3.34375 0.953125 -3.296875 0.953125 -3.125 C 0.953125 -3.078125 0.9375 -3.015625 0.9375 -2.984375 L 0.125 0 L 0.765625 0 C 1.15625 -1.34375 1.21875 -1.546875 1.609375 -2.109375 C 2.140625 -2.90625 2.53125 -3.328125 2.875 -3.328125 C 3 -3.328125 3.078125 -3.234375 3.078125 -3.078125 C 3.078125 -2.96875 3.015625 -2.671875 2.953125 -2.40625 L 2.578125 -1.015625 C 2.46875 -0.578125 2.4375 -0.46875 2.4375 -0.390625 C 2.4375 -0.0625 2.625 0.078125 2.84375 0.078125 C 3.25 0.078125 3.453125 -0.09375 4.03125 -0.890625 Z M 3.921875 -1 "/>
# </symbol>
# </g>
# </defs>
# <g id="surface1">
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph0-0" x="0.339844" y="17.171875"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph1-0" x="7.605469" y="14.132812"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph2-0" x="15.53125" y="17.171875"/>
# </g>
# <path style="fill:none;stroke-width:1.2;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 28.503906 -3.037865 L 91.785156 -3.037865 " transform="matrix(1,0,0,1,0,17.170677)"/>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph3-0" x="28.632812" y="2.369838"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph4-0" x="37.519531" y="12.104492"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph5-0" x="43.460938" y="12.104492"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph5-1" x="51.886719" y="12.104492"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph4-1" x="37.800781" y="5.198242"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph6-0" x="56.808594" y="2.656738"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph7-0" x="61.140625" y="8.785156"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph4-0" x="65.480469" y="11.862305"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph1-1" x="70.628906" y="8.785156"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph7-1" x="79.804688" y="8.785156"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph6-1" x="84.554688" y="2.656738"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph5-2" x="87.542969" y="5.405273"/>
# </g>
# <g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
#   <use xlink:href="#glyph7-2" x="58.066406" y="21.878906"/>
# </g>
# </g>
# </svg>
# 

# let's Calculate the Variance using the inbuilt function from the given data

# In[25]:


df.var()


# In[26]:


def variance(data):
    # no of observations
    n = len(data)
    mean = sum(data)/n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations)/n
    return variance

variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])


# # 5. Let's have a look on Standard Deviation and its functionality
# A standard deviation is a statistic that measures the dispersion of a dataset relative to its mean. The standard deviation is calculated as the square root of variance by determining each data point's deviation relative to the mean.
# If the data points are further from the mean, there is a higher deviation within the data set; thus, the more spread out the data, the higher the standard deviation.
# Standard deviation is the square root of variance $\sigma^2$ and is denoted as $\sigma$. So, if we want to calculate the standard deviation, then all we just have to do is to take the square root of the variance as follows:
# Lets have look on standard deviation formula
# Standard deviation$$\sigma = \sqrt{\sigma^2}$$

# In[27]:


df.std()


# In[42]:


import math

# We relay on our previous implementation for the variance

def variance(data, ddof=0):
        n = len(data)
        mean = sum(data) / n
        return sum((x - mean) ** 2 for x in data) / (n - ddof)
      def stdev(data):
        var = variance(data)
        std_dev = math.sqrt(var)
        return std_dev

        stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])


# # 6. Lets understand the correlation and its functionality
# Correlation shows the strength of a relationship between two variables and is expressed numerically by the correlation coefficient. The correlation coefficient's values range between -1.0 and 1.0.
# A perfect positive correlation means that the correlation coefficient is exactly 1. A perfect negative correlation means that two assets move in opposite directions, while a zero correlation implies no linear relationship at all.
# Following is the formula for calculating the correlation
# $$ r = \frac{\sum(X-X)*(Y-Y)}{\sqrt\sum(X-\bar{X}^2) * \sqrt(Y-\bar{Y}^2} $$

# In[43]:


df.corr()


# In[44]:



plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),annot=True)


# # 7. Lets calculate the Correlation coefficient without using the inbuilt function

# In[45]:


sample_df = pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns = list('ABCD'))


# In[46]:


sample_df


# In[47]:


def corr_coeff(df, x, y):
    
    x_bar = df[x].mean()
    y_bar = df[y].mean()
    
    ## lets calculate the std of two columns
    x_std = df[x].std()
    y_std = df[y].std()
    
    total_prod = (((df[x]-x_bar)/x_std)*((df[y]-y_bar)/y_std)).sum()
    corr = total.prod/(df.shape[0]-1)
    
    return corr


# In[48]:


sample_df.corr()


# # 8. Let's have a look and understand of Normal Distribution and its function
# The normal distribution is a continuous probability distribution that is symmetrical on both sides of the mean, so the right side of the center is a mirror image of the left side.
# The area under the normal distribution curve represents probability and the total area under the curve sums to one.
# Most of the continuous data values in a normal distribution tend to cluster around the mean, and the further a value is from the mean, the less likely it is to occur.
# For a perfectly normal distribution the mean, median and mode will be the same value, visually represented by the peak of the curve.
# Features of a Normal Distribution (Bell Curve)

# Lets have a look on the formula of Normal distribution
# $$ Z = \frac{X - \mu}{\sigma}$$
# Let's have of look on Normal distribution by ploting using sample random data

# In[49]:


from scipy.stats import norm
x = np.arange(-3,3,0.001)
plt.title('Normal distribution plot using pdf')
plt.xlabel('weight')
plt.ylabel('probability')
plt.plot(x,norm.pdf(x))
plt.show()


# Plotting a normal distribution plot using the distplot on given dataset

# In[50]:


import seaborn as sns
sns.set(color_codes=True)
sns.distplot(df['Mthly_HH_Income'])
plt.title('Normal distributed data')
plt.xlabel('Standard deviation')
plt.ylabel('probability')
plt.show()


# # 9. Let's us know about the features of Normal Distribution
# The Main features of Normal Distribution are follows
# 1. It is Symmentric
# A normal distribution comes with a perfectly symmentrical shape. This means that the distribution curve can be divided in the middle to produce two equal halves.
# 2. The Mean, Median, and Mode are equal
# The middle point of a normal distribution is the point with the maximum frequency, which means that it possesses the most observations of the variable. The measures are usually equal in a perfectly (normal) distribution.
# 3. Empirical rule
# In normally distributed data, there is a constant proportion of distance lying under the curve between the mean and specific number of standard deviations from the mean. For example, 68.25% of all cases fall within +/- one standard deviation from the mean. 95% of all cases fall within +/- two standard deviations from the mean, while 99% of all cases fall within +/- three standard deviations from the mean.
# 4. Skewness and kurtosis
# Skewness and kurtosis are coefficients that measure how different a distribution is from a normal distribution. Skewness measures the symmetry of a normal distribution while kurtosis measures the thickness of the tail ends relative to the tails of a normal distribution.
# 10. Let's have a understanding of positve and Negetive Skewed Normal Distribution
# Skewed Normal Distribution
# A Positive-skewed distribution has a long right tail. Positive-skewed distributions are also called Right-skew distributions. That’s because there is a long tail in the positive direction on the number line. The mean is also to the right of the peak.
# The value of skewness for a positively skewed distribution is greater than zero. As you might have already understood by looking at the figure, the value of mean is the greatest one followed by median and then by mode.
# A left-skewed distribution has a long left tail. Left-skewed distributions are also called negatively-skewed distributions. That’s because there is a long tail in the negative direction on the number line. The mean is also to the left of the peak.
# Negatively skewed distribution refers to the distribution type where the more values are plotted on the right side of the graph, where the tail of the distribution is longer on the left side and the mean is lower than the median and mode which it might be zero or negative due to the nature of the data as negatively distributed.
# 

# # 10. Let's have a understanding of positve and Negetive Skewed Normal Distribution
# Skewed Normal Distribution
# A Positive-skewed distribution has a long right tail. Positive-skewed distributions are also called Right-skew distributions. That’s because there is a long tail in the positive direction on the number line. The mean is also to the right of the peak.
# The value of skewness for a positively skewed distribution is greater than zero. As you might have already understood by looking at the figure, the value of mean is the greatest one followed by median and then by mode.
# A left-skewed distribution has a long left tail. Left-skewed distributions are also called negatively-skewed distributions. That’s because there is a long tail in the negative direction on the number line. The mean is also to the left of the peak.
# Negatively skewed distribution refers to the distribution type where the more values are plotted on the right side of the graph, where the tail of the distribution is longer on the left side and the mean is lower than the median and mode which it might be zero or negative due to the nature of the data as negatively distributed.
# 

# In[51]:


df.head()


# In[ ]:




