#!/usr/bin/env python
# coding: utf-8

# # Finding all occurence of substring in given string

# In[130]:


stre = 'what we think we become ; we are python programmer'
for each in range(0, len(stre)):
    if stre[each] == 'w' and stre[each+1] == 'e':
        print(each)


# In[135]:


Raghu = 'python is High level language , python is very intresting, python is easy'
for each in range(0, len(Raghu)):
    if Raghu[each] == 'i' and Raghu[each+1] == 's':
        print(each)


# # islower and isupper practice in assignment

# In[139]:


'raghu'.islower()


# In[140]:


'Mohith sir'.islower()


# In[141]:


'one milse is Rs 25'.islower()


# In[134]:


'Raghu'.isupper()


# In[137]:


'$500'.isupper()


# In[142]:


'RAVINDRANATH'.isupper()


# In[ ]:




