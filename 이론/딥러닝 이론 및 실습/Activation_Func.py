#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


def sigmoid(x):
    return 1/(1+np.exp(-x))
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

