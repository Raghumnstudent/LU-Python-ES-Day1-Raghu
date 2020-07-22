#!/usr/bin/env python
# coding: utf-8

# In[4]:


sum = 0
number = int(input('Enter the Number: '))
num = number
print(number)
while number != 0:
      sum = sum + number
      number = number - 1
print(f'Sum of {num} Number: {sum}')


# In[18]:


number = int(input('Enter the Number: '))
if number > 1:
    for i in range(2, number):
        if number%i == 0:
            print(number, 'is not Prime Number')
            break
    else:
        print(number, 'is Prime Number')
else:
    print(number, 'is not Prime Number')
    


# In[ ]:




