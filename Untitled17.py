#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))

