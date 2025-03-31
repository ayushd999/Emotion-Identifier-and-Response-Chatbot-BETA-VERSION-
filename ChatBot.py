import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import os
import time
import pandas as pd
import random
df = pd.read_csv(r"chatbot_sentiment_dataset.csv")
encoder = LabelEncoder()
df['Sentiment'].replace({'neutral' : 0 , 'negative' : 0 , 'positive' : 1 } , inplace = True)
vector = TfidfVectorizer(stop_words = "english" , max_features=5000)
x = df["User Message"]
x = vector.fit_transform(x)
y = df.iloc[: , 2:
model = LogisticRegression()
xtrain , xtest , ytrain , ytest = train_test_split(x , y , train_size=0.8 , test_size = 0.2)
model.fit(xtrain,ytrain)
model.predict(xtest)
model.score(xtest,ytest)
df1 = pd.read_csv(r"User_Messages.csv")
w = df1["User_Messages"]
w = vector.transform(w)
response = model.predict(w)
pos = pd.read_csv(r"positive.csv")
neg = pd.read_csv(r"negative.csv")
file_path = r"User_Messages.csv"
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


