#!/usr/bin/env python
# coding: utf-8

# In[2]:



a=input()
b=['a','e','i','o','u','A','E','I','O','U',' ']
d=""
for i in a:
    if i in b:
        d+=i
if(len(d)>0):
    print(d)
else:
    print('No Vowel')


# In[ ]:




