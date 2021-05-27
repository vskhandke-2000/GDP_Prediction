import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
dataset = pd.read_excel('Economy_Prediction_Dataset.xlsx')
#dataset.head()
#dataset.isnull().sum()
'''
dataset.isnull().sum() =>
Import in millions = 1
Export in millions = 1
Literacy rate = 23
Stock market sales = 5
Sensex Index(Gain/Loss) = 3
'''
dataset['Import in millions'].fillna(dataset['Import in millions'].mean(), inplace=True)
dataset['Export in millions'].fillna(dataset['Export in millions'].mean(), inplace=True)
dataset['Stock market sales'].fillna(dataset['Stock market sales'].mean(), inplace=True)
dataset['Sensex Index(Gain/Loss)'].fillna(dataset['Sensex Index(Gain/Loss)'].mean(), inplace=True)
dataset.drop(['Literacy rate','Gold rate(In Rs. /10grm 24 Karat)'], axis=1, inplace=True)
X = dataset.iloc[:, :10]
y = dataset.iloc[:,-1]


from sklearn.ensemble import RandomForestRegressor as rfr
model_1 = rfr(random_state=1)
model_1.fit(X, y)


pickle.dump(model_1, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
