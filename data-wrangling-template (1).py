#!/usr/bin/env python
# coding: utf-8

# # Data Wrangling Template

# ## Gather

# In[1]:


import pandas as pd
import zipfile


# In[2]:


# Extract all contents from zip file
with zipfile.ZipFile('armenian-online-job-postings.zip', 'r') as myzip:
    myzip.extractall()


# In[6]:


# Read CSV (comma-separated) file into DataFrame
df = pd.read_csv('online-job-postings.csv')
df.head()


# ## Assess

# In[ ]:





# ## Clean
# #### Define
# 
# #### Code

# In[ ]:





# #### Test

# In[ ]:




