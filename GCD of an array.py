#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
n=int(input())
a=list(map(int, input().split()))
if(n>=2):
    c=math.gcd(a[0],a[1])
    for i in range(n):
        c=(math.gcd(a[i],c))
    print(c)
else:
    print(a[0])


# In[ ]:




