#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


df = pd.read_csv(r"C:\Users\Ayush Das\Downloads\chatbot_sentiment_dataset.csv")
df


# In[3]:


encoder = LabelEncoder()
encoder


# In[4]:


df['Sentiment'].replace({'neutral' : 0 , 'negative' : 0 , 'positive' : 1 } , inplace = True)
df


# In[5]:


vector = TfidfVectorizer(stop_words = "english" , max_features=5000)
vector


# In[6]:


x = df["User Message"]
x = vector.fit_transform(x)
x


# In[7]:


y = df.iloc[: , 2:]
y


# In[8]:


model = MultinomialNB()
model


# In[9]:


xtrain , xtest , ytrain , ytest = train_test_split(x , y , train_size=0.8 , test_size = 0.2)
xtest


# In[10]:


model.fit(xtrain,ytrain)


# In[11]:


model.predict(xtest)


# In[12]:


model.score(xtest,ytest)


# In[13]:


df1 = pd.read_csv(r"C:\Users\Ayush Das\Desktop\User_Messages.csv")
df1


# In[16]:


w = df1["User_Messages"]
w = vector.transform(w)
response = model.predict(w) 


# In[23]:


pos = pd.read_csv(r"C:\Users\Ayush Das\Downloads\positive.csv")
neg = pd.read_csv(r"C:\Users\Ayush Das\Downloads\negative.csv")


# In[24]:


import os
import time
import pandas as pd
import random
file_path = r"C:\Users\Ayush Das\Desktop\User_Messages.csv"


# In[27]:


while True:
    while os.path.getsize(file_path) == 0:
        time.sleep(1)
    response = np.array(response).flatten()
    f1 = pos["Chatbot Response"].tolist()
    f2 = neg["Chatbot Response"].tolist()
    for val in zip(response):
        if val == 1:
            print(random.choice(f1))
        elif val == 0:
            print(random.choice(f2))
        else:
            print(random.choice(f1))
    open(file_path, "w").close()

    ch = input("Do you want me to answer next? (y/n): ").strip().lower()
    if ch != 'y':
        break


# In[ ]:




