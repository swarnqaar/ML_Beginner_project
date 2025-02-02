# -*- coding: utf-8 -*-
"""Rock vs Mine_prediction.ipynb
Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bYBI__r86EBnm8uHq2USBWcX3AE4NxKp

Project 1 ; ROCK vs MINE PREDICTION
"""

#importing the Dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading sonar dataset to the pandas dataframe
sonar_data = pd.read_csv('/content/sonar data.csv' , header=None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#separating data and labels
x = sonar_data.drop(columns=60 , axis=1)
y = sonar_data[60]

print(x)

print(y)

"""training and testing"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.1, stratify= y, random_state=1)

print(x.shape, x_train.shape, x_test.shape)

print(x_train)
print(x_test)

"""MODEL TRAINING --> LOGISTIC REGRESSION"""

model = LogisticRegression()

#training the logistic regression model with training data
model.fit(x_train, y_train)

"""MODEL EVOLUTION"""

#accuracy on the training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)
print('Accuracy on the training data:', training_data_accuracy)

#accuracy on the test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
print('Accuracy on the training data:', test_data_accuracy)

"""MAKING PREDICTIVE SYSTEM"""

input_data =(0.0200,0.0381,0.0428,0.0207,0.0954,0.0976,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)

#changing the input_data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)


if (prediction[0]=='R'):
  print('The prediction is a rock')
else:
  print('The object is a Mine')

