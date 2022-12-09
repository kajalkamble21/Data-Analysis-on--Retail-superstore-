#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("E:/KajalKamble/SampleSuperstore.csv")  # read superstore csv file


# In[ ]:





# In[4]:


df.head()    #display top 5 rows


# In[5]:


df.tail() 


# In[7]:


df.shape


# In[8]:


df.describe()     


# In[9]:


df.isnull().sum()    


# In[10]:


df.info()  


# In[11]:


df.isnull()


# In[12]:


df.columns


# In[13]:


df.duplicated().sum()


# In[14]:


df.nunique()


# In[17]:


df['Postal Code'] = df['Postal Code'].astype('object')


# In[16]:


df.drop_duplicates(subset=None,keep='first',inplace=True)
df.duplicated().sum()


# In[18]:


corr = df.corr()
sns.heatmap(corr,annot=True,cmap='Reds')


# In[19]:


df = df.drop(['Postal Code'],axis = 1)    #dropping postal code columns


# In[20]:


sns.pairplot(df, hue = 'Ship Mode')


# In[21]:


df['Ship Mode'].value_counts()


# In[22]:


sns.countplot(x=df['Ship Mode'])


# In[23]:


df['Segment'].value_counts()    


# In[24]:


sns.pairplot(df,hue = 'Segment')  


# In[25]:


sns.countplot(x = 'Segment',data = df, palette = 'rainbow')


# In[26]:


df['Category'].value_counts()


# In[27]:


sns.countplot(x='Category',data=df,palette='tab10')


# In[28]:


sns.pairplot(df,hue='Category')


# In[29]:


df['Sub-Category'].value_counts()


# In[30]:


plt.figure(figsize=(15,12))
df['Sub-Category'].value_counts().plot.pie(autopct='dark')
plt.show()


# In[31]:


df['State'].value_counts()


# In[32]:


plt.figure(figsize=(15,12))
sns.countplot(x='State',data=df,palette='rocket_r',order=df['State'].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# In[33]:


df.hist(figsize=(10,10),bins=50)
plt.show()


# In[34]:


plt.figure(figsize=(10,8))
df['Region'].value_counts().plot.pie(autopct = '%1.1f%%')
plt.show()


# In[35]:


#Profit vs Discount
fig,ax=plt.subplots(figsize=(20,8))
ax.scatter(df['Sales'],df['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[36]:


sns.lineplot(x='Discount',y='Profit',label='Profit',data=df)
plt.legend()
plt.show()


# In[37]:


#profit vs quantity
sns.lineplot(x='Quantity',y='Profit',label='Profit',data=df)
plt.legend()
plt.show()


# In[38]:


df.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['pink','blue'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[39]:


#Profit and sales are maximum in consumer segment and minimum in Home Office segment
plt.figure(figsize=(12,8))
plt.title('Segment wise Sales in each Region')
sns.barplot(x='Region',y='Sales',data=df,hue='Segment',order=df['Region'].value_counts().index,palette='rocket')
plt.xlabel('Region',fontsize=15)
plt.show()


# In[40]:


#Segment wise sells
df.groupby('Region')[['Profit','Sales']].sum().plot.bar(color=['blue','red'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[41]:


#Profit and sales are maximum in west region and minimum in south region
ps = df.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['blue','orange'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('States')
plt.ylabel('Profit/loss & Sales')
plt.show()


# In[44]:


#high profit is for california, new york
#loss is for texas, pennsylvania, Ohio
t_states = df['State'].value_counts().nlargest(10)
t_states


# In[45]:


df.groupby('Category')[['Profit','Sales']].sum().plot.bar(color=['yellow','purple'],alpha=0.9,figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[46]:


#Technology and Office Supplies have high profit.
#Furniture have less profit
ps = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['red','lightblue'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/loss & Sales')
plt.show()


# In[ ]:




