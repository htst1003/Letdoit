#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from shapely.geometry import Point 
import geopandas as gpd 
from geopandas import GeoDataFrame 


# In[78]:


df=pd.read_csv('DPFONAL_1.csv')


# ### Produce the frequency table of “CRCLSCOD” with the following columns: 
# ### (1)  each category of this predictor and 
# ### (2) the frequency of each level of this predictor.

# In[79]:


freq = pd.crosstab(index=df["crclscod"], columns="count") 
freq.sort_values('count',ascending=False,inplace=True)
#freq.reset_index()
# create freq table


# In[80]:


freq


# In[81]:


len(pd.unique(freq.index))


# ### What is the cardinality of this predictor “CRCLSCOD “?  54 cardinality
# ### What is the threshold set by you to combine all cells with frequency less than this threshold?  just 120???
# ### How many categories of this predictor has cell frequency less than the threshold set by you?  29 categories
# ### Combine categories with frequency less than the threshold set by you.

# In[82]:


freq['count'].sum()
# check total number of count


# In[83]:


freq.loc[freq['count']<120].sum()
# check total number of count under 120


# In[92]:


freq.drop(freq[freq['count'] < 120].index, inplace = True)
freq.loc['combined']= [1044]
freq
#drop rows under 120 count, and add new row with sum of removed rows


# In[93]:


freq['count'].sum()
#check if total is same as previous total
##Combine categories with frequency less than the threshold set by you.  -COMPLETE


# ### Produce another table that has the following columns: (1) each remaining category from Part (b); 
# ### (2) frequency; (3) proportion of “Churn=1” (i.e., Churn Rate); 
# ### (4) Lower Bound of Churn Rate, (5) Upper Bound of Churn Rate; and (6) width 95% Confidence Interval.

# In[ ]:





# In[ ]:





# In[ ]:





# # Problem 3 (10) 
# ### Use difference dummy coding for the predictor “Marital” (ignore the missing cell).  
# ### Report the dummy coding table that is similar to page 52 of lecture note. -Difference dummy coding: Compare each level with the average of previous levels.
# 

# In[111]:


prob3 = pd.crosstab(index=df["marital"], columns="count") 
print(len(pd.unique(prob3.index)))
prob3
#check the marital column


# In[99]:


prob3.isnull().sum() 
#check if there is missing data. None.


# In[105]:


prob3=prob3.reset_index()


# In[106]:


pd.get_dummies(prob3['marital']).head()


# In[113]:


prob3 = pd.crosstab(index=prob3["marital"], columns="count") 


# In[ ]:




