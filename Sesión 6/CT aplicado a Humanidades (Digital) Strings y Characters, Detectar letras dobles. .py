#!/usr/bin/env python
# coding: utf-8

# In[ ]:


len ('hello world')


# In[3]:


hi = 'hello world'
len(hi)


# In[6]:


'hello'[4]


# In[8]:


'hello'[1:3]


# In[9]:


'hello world'[1:]


# In[12]:


original = 'Burma Shave'
lowercase = original.lower()
lowercase


# In[13]:


wyatt = 'They flee from me that sometime did me seek / With naked foot, stalking in my chamber'
wyatt = wyatt.lower()
wyatt


# In[16]:


for i in range(len(wyatt)): 
    print(wyatt[i])


# In[20]:


for i in range(len(wyatt)): 
    print (i,wyatt[i]) 


# In[21]:


for i in range(len(wyatt)): 
    print(wyatt[i:i+2])


# In[24]:


par=0
for i in range(len(wyatt)): 
    if wyatt[i:i+2]== 'ee':
        par=par+1
par


# In[27]:


par=0
for i in range(len(wyatt)-1): 
    if wyatt[i]== wyatt[i+1]:
        par=par+1
par


# In[ ]:




