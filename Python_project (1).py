#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[ ]:





# # Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(color_codes = True)

import warnings
warnings.filterwarnings("ignore")


# ### Import Data Set

# In[2]:


df=pd.read_csv("sport car price.csv")
df


# #### Data Understanding

# In[3]:


df.head(5)


# In[4]:


df.shape


# In[5]:


df.info


# In[6]:


#removing commas from price column
df['Price (in USD)']=df['Price (in USD)'].str.replace(",","")


# In[7]:


df['Price (in USD)']


# In[8]:


#converting price column to integer
df['Price (in USD)']=df['Price (in USD)'].apply(int)


# In[9]:


#changing the data into float
df['0-60 MPH Time (seconds)']=df['0-60 MPH Time (seconds)'].str.replace("<","")
df['0-60 MPH Time (seconds)']=df['0-60 MPH Time (seconds)'].apply(float)


# In[10]:


#Converting data to integer
df['Torque (lb-ft)']=df['Torque (lb-ft)'].str.replace(",","").str.replace("+","")
df['Torque (lb-ft)']=df['Torque (lb-ft)'].str.replace("-","0")
df['Torque (lb-ft)']=df['Torque (lb-ft)'].fillna("0")
df['Torque (lb-ft)']=df['Torque (lb-ft)'].apply(int)


# In[11]:


df['Horsepower']=df['Horsepower'].str.replace("+","").str.replace(',',"")
df['Horsepower']=df['Horsepower'].apply(int)


# # Segment engine size

# In[12]:


df['Engine Size (L)'].unique()


# In[13]:


# Define a function to segment the values
def segment_engine_size(engine_size):
    if engine_size in ['Electric','Hybrid']:
        return 'Electric/Hybrid'
    elif engine_size in ['Electric (93 kWh)' ,'Electric (100 kWh)' ,'Electric (tri-motor)','Electric Motor','2.0 (Electric)']:
        return 'Electric'
    elif engine_size == '1.5 + Electric':
        return '1.5 Hybrid'
    elif engine_size in ['Hybrid (4.0)','4.0 (Hybrid)']:
        return '4.0 Hybrid'
    elif engine_size == '0':
        return 'Unknown'
    elif engine_size == '-':
        return 'unknown'
    elif float(engine_size) < 2 :
        return 'small'
    elif float(engine_size) < 3 :
        return 'medium'
    else :
        return 'Large'
    
df['Engine Size (L)']=df['Engine Size (L)'].apply(segment_engine_size)
df['Engine Size (L)'].unique()


# #### Distribution of engine size segment

# In[14]:


plt.figure(figsize=(14,7))
ax=sns.countplot(data=df,x=df['Engine Size (L)'], order=df['Engine Size (L)'].value_counts().index)
plt.title("Distribution of engine size segment",pad=12,fontsize=15,weight="bold")
plt.xticks(weight="bold")
plt.yticks(weight="bold")
plt.xlabel("Engine Size",weight="bold",fontsize = 14  , labelpad=8)
plt.ylabel
for i in ax.containers:
    i.datavalues
    ax.bar_label(i,weight="bold")
plt.show()


# In[15]:


#find data types after changing the data types
df.dtypes


# In[16]:


df.describe()


# In[17]:


df.describe(include=object)


# In[18]:


df.loc[df.duplicated().sum()]


# In[19]:


df.isna().sum()


# #### Removing irrelevant columns

# In[20]:


df.head()


# In[21]:


df['Car Model'].value_counts()


# In[22]:


df.drop(columns='Car Model',inplace=True)


# In[23]:


df.head(5)


# #### Segmant car Make

# In[24]:


df['Car Make'].unique()


# In[25]:


def segment_car_make(car_make):
    if car_make in ['Porsche', 'Lamborghini', 'Ferrari','McLaren','Aston Martin','Bugatti','Bugatti']:
        return 'Luxury'
    elif car_make in ['Audi',  'BMW','Mercedes-Benz','Chevrolet', 'Ford', 'Nissan','Dodge', 'Jaguar','Mercedes-AMG']:
        return 'Mainstreams'
    elif car_make in ['W Motors','Ariel','Shelby', 'TVR','Subaru', 'Alpine', 'Ultima']:
        return 'Speciality'
    else:
        return 'Other'
df['Car Make']=df['Car Make'].apply(segment_car_make)
df['Car Make'].unique()


# #### Distribution of car segments

# In[26]:


plt.figure(figsize=(14,7))
ax=sns.countplot(data=df,x=df['Car Make'], order=df['Car Make'].value_counts().index)
plt.title("Distribution of car segment",pad=12,fontsize=15,weight="bold")
plt.xticks(weight="bold")
plt.yticks(weight="bold")
plt.xlabel("car segment",weight="bold",fontsize = 14  , labelpad=8)
plt.ylabel
for i in ax.containers:
    i.datavalues
    ax.bar_label(i,weight="bold")
plt.show()


# #### Distribution of car category in price

# In[27]:


plt.figure(figsize=(14,7))
sns.barplot(data=df,x=df['Car Make'], y=df['Price (in USD)'], order=df['Car Make'].value_counts(ascending=True).index)
plt.title("Distribution of car category in price",pad=12,fontsize=15,weight="bold")
plt.xticks(weight="bold")
plt.yticks(weight="bold")
plt.xlabel("car category",weight="bold",fontsize = 12  , labelpad=12)
plt.ylabel("Price (in USD)",weight="bold",fontsize = 12  , labelpad=12)
for i in ax.containers:
    i.datavalues
    ax.bar_label(i,weight="bold")
plt.show()


# #### Distribution of Engine size in price

# In[28]:


plt.figure(figsize=(14,7))
sns.barplot(data=df,x=df['Engine Size (L)'], y=df['Price (in USD)'], order=df['Engine Size (L)'].value_counts().index)
plt.title("Distribution of Engine size in price",pad=12,fontsize=15,weight="bold")
plt.xticks(weight="bold")
plt.yticks(weight="bold")
plt.xlabel("Engine Size (L)",weight="bold",fontsize = 12  , labelpad=12)
plt.ylabel("Price (in USD)",weight="bold",fontsize = 12  , labelpad=12)
for i in ax.containers:
    i.datavalues
    ax.bar_label(i,weight="bold")
plt.show()


# In[ ]:




