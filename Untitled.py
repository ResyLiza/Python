#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
netflix = pd.read_csv(r"C:\Users\Resy\Documents\New Folder\netflix_titles.csv")
print(netflix)


# In[3]:


netflix = pd.read_csv(r"C:\Users\Resy\Documents\New Folder\netflix_titles.csv")
print(netflix)


# In[4]:


netflix.keys()


# In[5]:


netflix.head(5)


# In[8]:


netflix.tail()


# In[9]:


netflix.info()


# In[12]:


netflix[netflix.duplicated()]


# In[14]:


netflix.isnull()


# In[15]:


netflix.isnull().sum()


# In[17]:


import seaborn as sns
sns.heatmap(netflix.isnull())


# In[18]:


netflix.head(10)


# In[23]:


netflix[(netflix['title']).isin(['The Starling'])]


# In[24]:


netflix['Date_N'] = pd.to_datetime(netflix['date_added'])


# In[25]:


netflix.head(5)


# In[26]:


netflix.dtypes


# In[28]:


netflix['Date_N'].dt.year.value_counts()


# In[32]:


netflix['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[39]:


netflix.head(5)


# In[41]:


netflix.groupby('type').type.count()


# In[35]:


sns.countplot(netflix['type'])


# In[61]:


netflix.groupby('release_year').release_year.count()


# In[46]:


netflix.head(5)


# In[51]:


netflix(netflix['type'] == 'title') & (netflix['release_year']==2000.0)


# In[73]:


netflix[(netflix['type']=='Movie')&(netflix['release_year']==2021)]


# In[77]:


netflix[(netflix['type']=='Movie')&(netflix['country']=='Indonesia')]


# In[92]:


pip install plotly.express 


# In[93]:


import plotly.express as px


# In[81]:


country_count=netflix['country'].value_counts().sort_values(ascending=False)
country_count=pd.DataFrame(country_count)
topcountries=country_count[0:5]
topcountries


# In[90]:


import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style


# In[99]:


data = dict(
    number=[2818,972,419,245,199],
    country=["United States", "India", "United Kingdom", "Japan","Canada"])
fig = px.funnel(data, x='number', y='country')
fig.show()


# In[121]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[193]:


top_year = netflix.groupby('release_year').count().sort_values('title',ascending=False).head()
top_year.reset_index(inplace=True)
top_year


# In[158]:


plt.figure(figsize=(10,8))
sns.countplot(netflix['release_year'])


# In[263]:


plt.figure(figsize=(10,6))
netflix_rating = netflix['rating'].value_counts()
netflix_rating = pd.DataFrame(netflix_rating).reset_index()
netflix_rating.columns = ['rating','Nbr']
sns.barplot(x = 'Nbr',y = 'rating', data=netflix_rating.head(10), palette='dark:salmon_r');
plt.show()


# In[219]:


netflix_genre = netflix['listed_in'].value_counts()
netflix_genre = pd.DataFrame(netflix_genre).reset_index()
netflix_genre.columns = ['listed_in','Nbr']


# In[260]:


plt.figure(figsize=(10,6))
plt.xticks(rotation = 'vertical')
sns.barplot(x = 'Nbr',y = 'listed_in', data=netflix_genre.head(7) ,palette='Greens_r', saturation=.4,);
plt.show()


# In[248]:


netflix_actor = netflix['cast'].value_counts()
netflix_actor = pd.DataFrame(netflix_actor).reset_index()
netflix_actor.columns = ['cast','Nbr']


# In[264]:


plt.figure(figsize=(10,6))
plt.xticks(rotation = 'vertical')
sns.barplot(x = 'Nbr',y = 'cast', data=netflix_actor.head(7) , palette='copper',saturation=.4,);
plt.show()


# In[242]:


actor_count=netflix['cast'].value_counts().sort_values(ascending=False)
actor_count=pd.DataFrame(actor_count)
topactor=actor_count[0:5]
topactor


# In[266]:


type_count=netflix['type'].value_counts().sort_values(ascending=False)
type_count=pd.DataFrame(type_count)
toptype=type_count[0:5]
toptype


# In[278]:


director_count=netflix['director'].value_counts().sort_values(ascending=False)
director_count=pd.DataFrame(director_count)
topdirector=director_count[0:10]
topdirector


# In[282]:


netflix_director = netflix['director'].value_counts()
netflix_director = pd.DataFrame(netflix_director).reset_index()
netflix_director.columns = ['director','Nbr']


# In[293]:


plt.figure(figsize=(15,6))
plt.xticks(rotation = 'horizontal')
sns.barplot(x = 'director',y = 'Nbr', data=netflix_director.head(7) , palette='crest',saturation=.5,);
plt.show()


# In[ ]:




