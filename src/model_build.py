import pandas as pd
import numpy as np
import os
import sklearn

from sklearn.ensemble import RandomForestClassifier
import pickle

train_data = pd.read_csv('./data/processed/train_processed.csv')

# x_train = train_data.iloc[:, 0:-1].values
# y_train = train_data.iloc[:, -1].values
x_train = train_data.drop(columns=['Potability'], axis=1)
y_train = train_data['Potability']

clf = RandomForestClassifier()
clf.fit(x_train, y_train)

#save
pickle.dump(clf, open('model.pkl', 'wb'))