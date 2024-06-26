import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y))
y = np.array([np.where(labels == x) for x in y]).flatten()

# Use RandomForestClassifier instead of LogisticRegression
model = RandomForestClassifier().fit(X, y)

with open("model.pkl", 'wb') as f:
   pickle.dump(model, f)
