#!/usr/bin/env python
# coding: utf-8

"""
 Name : Vaishnavi Madhekar
 Roll No: 3429
 Div : B
 C No : C22018221438

 Problem statement : Apriori algorithm
"""


# In[1]:


pip install apyori


# In[2]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from apyori import apriori
from scipy.io import arff


# In[4]:


df = pd.read_csv('ContactLens.csv')


# In[5]:


df


# In[6]:


df.head()


# In[7]:


df.shape


# In[10]:


df.info()


# In[12]:


df.describe()


# In[14]:


get_ipython().run_cell_magic('time', '', 'records = []\nfor i in range(0,df.shape[0]):\n    records.append([str(df.values[i,j]) for j in range(df.shape[1])])')


# In[15]:


records


# In[17]:


get_ipython().run_cell_magic('time', '', '#Building the apriori model\nassociation_rules = apriori(records, min_support = 0.15, min_confidence = 0.1)\nassociation_results = list(association_rules)')


# In[18]:


#Getting the number of rules
print(len(association_results))


# In[19]:


association_results


# In[ ]:




