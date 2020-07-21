#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello Raghu')


# In[7]:


#escase usage
print('I\'a Raghu')


# In[18]:


print('Hello\nRaghu')


# In[19]:


print('Hello\aRaghu') # this give the sound if you run this code in command prompt


# In[10]:


print("Hello        Raghu")


# # if we want to print hard string or make documentation during code use these thrible quotes

# In[15]:


print(""" |\   /| \|_|/
  /. .\
 =\_Y_/= {>o<}  """)
print(""" thrible quotes is used for documentation and printing hard string""")


# In[21]:


name = 'Raghu'
age = 21
score = 9.656
Hobby = 'learning new things'
print('My name is ', name, 'age is ',age, 'score is ',score , 'Hobby is ',Hobby )


# In[27]:


print('My name is %5s   age is %5d  score is %5.2f  Hobby is %5s' %(name, age, score, Hobby)) # %5  is used to generate space


# In[30]:


print(f'My name is {name}  age is {age}  score is {score}  Hobby is {Hobby}')


# In[8]:


a = 45
b = 87
c = 2
d = 5
print(a + b)
print(b - a)
print(a / d)
print(d ** c)
print(b // d)
print(b / d)


# In[3]:


a = 10
b = 20
a == b


# In[4]:


c = 10
a==c


# In[5]:


c <= b


# In[6]:


c >= b


# In[7]:


c != b


# In[31]:


c = 23
d = 46
print(c | d) # Or operation
print(c & d) # and operation
print(c ^ d) # xor operation
print(~c)    # not operation
print(c >> 2) # right shift by 2 bits
print(d << 2) # left shift by 2 bits


# In[32]:


g = 2
h = 0
print(g and h)
print(g or h)
print(not h)


# In[36]:


a = 28
b = 28
print(a is b)
id(a)


# In[37]:


id(b) # here both the id is same so it return true


# In[43]:


r = -8    # numbers between -5 to 256 interpreter allocate same memory location if both are same number
t = -8    # number -8 is not in range so it allocate  different location 
print(r is t)


# In[44]:


id(r)


# In[45]:


id(t)


# In[33]:


name = 'Raghu M N'
print('a' in name)
print('M' not in name )


# In[46]:


print(2**-1)


# In[47]:


print(10+24/90*2)


# In[ ]:




