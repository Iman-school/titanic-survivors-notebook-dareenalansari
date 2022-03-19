#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df=pd.read_csv('titanic-passengers.csv', sep=';')
df.head()


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


df=pd.read_csv('titanic-passengers.csv', sep=';')
df.head(20)


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[8]:


df['Age'].isnull().sum()


# In[9]:


df['Cabin'].isnull().sum()


# In[10]:


df['Embarked'].isnull().sum()


# In[11]:


numeric=df.select_dtypes(include=np.number)
numeric_colums=numeric.colums


# In[ ]:


numeric


# In[ ]:


df['Age'].fillna(df['Age'].mean(),inplace=True)
df.head()


# In[ ]:


df=df.fillna(df.mode().iloc[0])
df.head()


# In[ ]:


df.info()


# In[ ]:


df.drop('Cabin',axis=1,inplace=True)


# In[ ]:


df.info()


# In[12]:


def create_fam_size(df):
    return df["SibSp"] + df["Parch"] + 1

df["family_size"] = create_fam_size(df)


# In[13]:


import re
def create_categorical_title(df):
    def find_title(name: str) -> str:
        search = re.search(
            " ([A-Za-z]+)\.", name
        )  # Search for a word with a point at the end
        if search:
            title = search.group(1)
            if title in ["Mlle", "Ms"]:
                return "Miss"
            elif title in ["Mme", "Mrs"]:
                return "Mrs"
            elif title == "Mr":
                return "Mr"
            else:
                return "Rare"
        return ""

    return_title = df["Name"].apply(find_title)
    dict_title = {"Miss": 1, "Mrs": 2, "Mr": 3, "Rare": 4}
    return return_title.replace(dict_title)


df["Title"] = create_categorical_title(df)


# In[19]:


df.head()


# In[25]:


df['person'].value_counts() #Get a number of male and female


# In[21]:


df['Alone'] = df.Parch + df.SibSp


# In[22]:


# if Alone value is >0 then they are with family else they are Alone


df['Alone'].loc[df['Alone']>0] = 'With Family'
df['Alone'].loc[df['Alone'] == 0] = 'Without Family'


# In[23]:


df.head()


# In[26]:


df["Survived"].value_counts() #Get a number of who is Survived or not


# In[27]:


cleanup_Survived = {"Survived":{"No": 0, "Yes": 1}}


# In[28]:


cleanup_Sex = {"person":     {"female": 0, "male": 1, "child": 3}}


# In[29]:


df = df.replace(cleanup_Sex)
df.head()


# In[30]:


df["Embarked"].value_counts()


# In[31]:


cleanup_Embarked = {"Embarked":     {"S": 1, "C": 2 , "Q": 3}}


# In[32]:


df = df.replace(cleanup_Embarked)
df.head(10)


# In[33]:


df["Alone"].value_counts()


# In[34]:


cleanup_Alone = {"Alone":     {"With Family": 1, "Alone": 0}}


# In[35]:


df = df.replace(cleanup_Alone)
df.head(10)


# In[ ]:




