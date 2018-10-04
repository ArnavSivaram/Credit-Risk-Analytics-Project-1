
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.style.use('seaborn')

#importing data
data1=pd.read_csv("../input/Data File.csv",encoding='latin-1',low_memory=False)
data1.head()


# In[ ]:


data1.shape


# In[ ]:


data1.describe(include='all')


# In[ ]:


print(data1.isnull().sum()/data1.shape[0]*100)


# In[ ]:


data2 = data1.loc[:, data1.isnull().sum() < 0.8*data1.shape[0]]


# In[ ]:


data2.shape


# In[ ]:


data2.describe(include='all')


# In[ ]:


h={}
ctr1=0
ctr2=0
for i in range(54):
    if isinstance(data2[data2.columns[i]].dropna().iloc[1],str):
        h[data2.columns[i]]=data2[data2.columns[i]].mode()[0]
        ctr1=ctr1+1
    else:
        h[data2.columns[i]]=data2[data2.columns[1]].median()
        ctr2=ctr2+1
print(ctr1)
print(ctr2)


# In[ ]:


data2.fillna(h,inplace=True)


# In[ ]:


data2.head()


# In[ ]:


print(data2.shape)
data2.describe(include='all')
print(data2.isnull().sum()/data2.shape[0]*100,"%")


# In[ ]:


sns.boxplot(data2['installment'])


# In[ ]:


ctr1=0
ctr2=0
for i in range(54):
    if isinstance(data2[data2.columns[i]].iloc[1],str):
        ctr1+=1
    else:
        q1=data2[data2.columns[i]].quantile(0.25)
        q3=data2[data2.columns[i]].quantile(0.75)
        iqr=q3-q1
        low=q1-1.5*iqr #acceptable range - windsorizing technique
        high=q3+1.5*iqr#acceptable range - windsorizing technique
        data2[data2.columns[i]].replace(data2[data2.columns[i]]<low,low)
        data2[data2.columns[i]].replace(data2[data2.columns[i]]>high,high)
        ctr2+=1
print(ctr1,ctr2)


# In[ ]:


ctr1=0
ctr2=0
for i in range(54):
    if isinstance(data2[data2.columns[i]].iloc[1],str):
        ctr1+=1
    else:
        data2 = pd.data2[data2.columns[i]].(mstats.winsorize(data2[data2.columns[i]], limits=[0.05, 0.05]))
        ctr2+=1
print(ctr1,ctr2)

