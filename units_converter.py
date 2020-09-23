#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import time
conversions = {
                "mm": {"mm": 1, "cm": 1/10, "m": 1/1000, "km": 1/1000000},
                "cm": {"mm": 10, "cm": 1, "m": 1/100, "km": 1/100000},
                "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 1/1000},
                "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
              }
    
while True:
    try:
        unit1 = raw_input ("Which unit would you like to convert from?\n
                           We support: " + ", .join(conversions.keys())).lower()"
        unit2 = raw_input ("Which unit would you like to convert to?\m
                           We support: " + ", .join(conversions[unit1].keys())).lower()")
        convert = conversions[unit1][unit2]
    except KeyError:
        print ("That is not a valid key, please try again")


# In[31]:


import math
import time

print ("Temperature Converter\nWe support \"С\" - Celsius, \"F\" - Fahrenheit")
unit1 = input ("Which unit would you like to convert from: ")
unit2 = input ("Which unit would you like to convert to: ")
num1 = float(input ("Enter your value: " ))

if unit1 == "C" and unit2 == "F":
    ans = num1*(9/5) + 32       
elif unit1 == "F" and unit2 == "C":
    ans = (num1 - 32)*5/9
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000  
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
print(ans)


# In[ ]:


conversions = {
                "mm": {"mm": 1, "cm": 1/10, "m": 1/1000, "km": 1/1000000},
                "cm": {"mm": 10, "cm": 1, "m": 1/100, "km": 1/100000},
                "m":  {"mm": 1000, "cm": 100, "m": 1, "km": 1/1000},
                "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
              }
unit1 = input ("Which unit would you like to convert from?\n We support: " + ", ".join(conversions.keys()))
unit2 = input ("Which unit would you like to convert to?\n We support: " + ", ".join(conversions[unit1].keys()))
    
while True:
    try:
        unit1 = input ("Which unit would you like to convert from?\n We support: "
                           ", ".join(conversions.keys())).lower()
        unit2 = input ("Which unit would you like to convert to?\m We support: "
                           ", ".join(conversions[unit1].keys())).lower()
        convert = conversions[unit1][unit2]
    except KeyError:
        print ("That is not a valid key, please try again")


# In[14]:


import math
import time
"""Unit Converter"""
#Welcome and variable setting

types = {
    "k": 1000,
    "h": 100,
    "da": 10,
    "": 1,
    "d": 0.1,
    "c": 0.01,
    "m": 0.001
}

def convert(from_unit_type, to_unit_type, value):
    from_type_units = types[from_unit_type]
    to_type_units = types[to_unit_type]

    new_value = value * (from_type_units / to_type_units)

    return str(new_value) + to_unit_type

print ("Unit Converter")
cat = input ("Which category would you like to convert? [g,l,m]")

unit1 = input ("Which unit would you like to convert from: ")
unit2 = input ("Which unit would you like to convert to: ")
num1 = input ("Enter your value: " )

print(convert(unit1, unit2, float(num1)))


# In[ ]:


import math
import time
unit1 = input ("Which unit would you like to convert from: ")
unit2 = input ("Which unit would you like to convert to: ")
num1 = input ("Enter your value: " )
def convert_SI(val, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[unit_in]/SI[unit_out]


# In[ ]:


import math
import time
def convert_SI(val, unit_in, unit_out):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[unit_in]/SI[unit_out]
unit1 = input ("Which unit would you like to convert from: ")
unit2 = input ("Which unit would you like to convert to: ")
num1 = input ("Enter your value: " )

