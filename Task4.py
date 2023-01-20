#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


d=pd.read_csv('C:/Users/Sapna vijay/OneDrive/Desktop/datasets/globalterrorismdb_0718dist.csv',encoding='latin1')
d


# In[4]:


d.describe()


# In[5]:


d.shape


# In[6]:


d.info()


# In[7]:


year=d['iyear'].unique()
year_count=d['iyear'].value_counts(dropna=False).sort_index()
plt.figure(figsize=(19,11))
sns.barplot(x=year,y=year_count,palette="tab10")
plt.xticks(rotation=50)
plt.xlabel('Attacking year',fontsize=20)
plt.ylabel('no. of attacks in that year',fontsize=20)
plt.title('Attacks in Year',fontsize=50)
plt.show()


# In[8]:


pd.crosstab(d.iyear,d.region_txt).plot(kind='area',stacked=False,figsize=(20,10))
plt.title('Terrorist Activities by ragion in a year',fontsize=20)
plt.xlabel('year',fontsize=20)
plt.ylabel('No.of attacks',fontsize=20)
plt.show()


# In[9]:


attack=d.country_txt.value_counts()[:20]
attack


# In[10]:


d.gname.value_counts()[1:10]


# In[11]:


plt.subplots(figsize=(20,10))
sns.barplot(d['country_txt'].value_counts()[:10].index,d['country_txt'].value_counts()[:10].values,palette='YlOrBr_r')
plt.title('Top countries Affected')
plt.xlabel('Countries')
plt.ylabel('Attacks')
plt.show()


# In[12]:


df = d[['iyear','nkill']].groupby(['iyear']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4)
plt.xticks(rotation = 50)
plt.title("People Died Due To Attack",fontsize=25)
plt.ylabel("Number of killed peope",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)
     


# In[13]:


d['city'].value_counts().to_frame().sort_values('city',axis=0,ascending=False).head(10).plot(kind='bar',figsize=(20,10),color='red')
plt.xticks(rotation = 50)
plt.xlabel("City",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("Top 10 most effected city",fontsize=20)
plt.show()


# In[14]:


d[['attacktype1_txt','nkill']].groupby(["attacktype1_txt"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['darkslateblue'])
plt.xticks(rotation=50)
plt.title("Number of killed ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()


# In[15]:


d[['attacktype1_txt','nwound']].groupby(["attacktype1_txt"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['cyan'])
plt.xticks(rotation=50)
plt.title("Number of wounded  ",fontsize=20)
plt.ylabel('Number of people',fontsize=15)
plt.xlabel('Attack type',fontsize=15)
plt.show()
     


# In[16]:


plt.subplots(figsize=(20,10))
sns.countplot(d["targtype1_txt"],order=d['targtype1_txt'].value_counts().index,palette="gist_heat",edgecolor=sns.color_palette("mako"));
plt.xticks(rotation=90)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.title("Attack per year",fontsize=20)
plt.show()


# In[17]:


d[['gname','nkill']].groupby(['gname'],axis=0).sum().drop('Unknown').sort_values('nkill',ascending=False).head(10).plot(kind='bar',color='yellow',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("No of killed people",fontsize=15)
plt.show()


# In[18]:


df=d[['gname','country_txt','nkill']]
df=df.groupby(['gname','country_txt'],axis=0).sum().sort_values('nkill',ascending=False).drop('Unknown').reset_index().head(10)
df


# In[19]:


kill = d.loc[:,'nkill']
print('Number of people killed by terror attack:', int(sum(kill.dropna())))


# In[20]:


typeKill = d.pivot_table(columns='attacktype1_txt', values='nkill', aggfunc='sum')
typeKill


# In[21]:


countryKill = d.pivot_table(columns='country_txt', values='nkill', aggfunc='sum')
countryKill
     


# Conclusion Ans Results
# 
# Country with the most attacks: Iraq
# 
# City with the most attacks: Baghdad
# 
# Region with the most attacks: South Asia
# 
# Year with the most attacks: 2014
# 
# Group with the most attacks: Islamic state of iraq and the levent (ISIL)
# 
# Most Attack Types: Armed Assault
# 
# Thank You
