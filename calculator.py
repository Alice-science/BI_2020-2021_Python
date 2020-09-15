#!/usr/bin/env python
# coding: utf-8

# In[26]:


import math
print('Use . as decimal separator')
a = float(input('number: '))
operator = input('operator: ')

if operator == "+":
    b = float(input('number: '))
    print(a + b)
elif operator == "-":
    b = float(input('number: '))
    print(a - b)
    
elif operator == "**" or operator == "^":
    b = float(input('number: '))
    print(a ** b)
    
elif operator == "!":
    print(math.factorial(a))

elif operator == "*":
    b = float(input('number: '))
    print(a * b)
elif operator == "/" or operator == ":":
    b = float(input('number: '))
    print(a / b)
else:
    print ('Try another operator')

