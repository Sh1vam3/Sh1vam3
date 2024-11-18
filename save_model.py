# -*- coding: utf-8 -*-
"""Heart_disease_Logistic_Regression_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lTV4TcoZn1zW1vt5g3Aby1oVvGULoEkG
"""
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score , accuracy_score,confusion_matrix , roc_curve , roc_auc_score , classification_report

# Load the model directly from the local file
import pickle




df = pd.read_csv('heart_disease.csv')
df.head()
with open("heart_disease.pkl", "rb") as file:
    model = pickle.load(file)
"""# EDA"""

print(df.describe())

print(df.shape)

sns.pairplot(df[['age','cp','thalach','target']])

X=df[['age','cp','thalach']]
y=df[['target']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:,1]

y_pred

print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

def predict_heart_disease():
    age = int(input("Enter your age: "))
    cp = int(input("Enter your chest pain type (0-3): "))
    thalach = int(input("Enter your maximum heart rate achieved: "))

    # Create a DataFrame with user input values, not column names
    user_data = pd.DataFrame([[age, cp, thalach]], columns=['age', 'cp', 'thalach'])

    prediction = model.predict(user_data)
    result = "heart disease" if prediction[0] == 1 else "no heart disease"
    print(f'prediction: {result}')

# Call the function
predict_heart_disease()
with open('heart_disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Model saved as 'heart_disease_model.pkl'")