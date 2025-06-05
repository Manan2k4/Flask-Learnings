import os
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# 1. Load dataset - UPDATE THIS PATH TO YOUR ACTUAL DATASET
dataset_path = os.path.join("data", "adult.csv")  # Or full path like r"C:\path\to\adult.csv"
try:
    df = pd.read_csv(dataset_path)
except FileNotFoundError:
    print(f"Error: Dataset not found at {dataset_path}")
    exit()

# 2. Data preprocessing (your existing code)
df.replace("?", np.nan, inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)

# Discretization
df.replace(['Divorced', 'Married-AF-spouse', 'Married-civ-spouse', 
            'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed'],
           ['divorced', 'married', 'married', 'married', 
            'not married', 'not married', 'not married'], inplace=True)

# Label Encoding
category_col = ['workclass', 'race', 'education', 'marital-status', 'occupation',
                'relationship', 'gender', 'native-country', 'income']
label_encoder = preprocessing.LabelEncoder()

for col in category_col:
    df[col] = label_encoder.fit_transform(df[col])

# Drop columns
df.drop(['fnlwgt', 'educational-num'], axis=1, inplace=True)

# 3. Split data
X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

# 4. Train model - THIS WAS MISSING
dt_clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=5, min_samples_leaf=5)
dt_clf_gini.fit(X_train, y_train)

# 5. Evaluate
y_pred_gini = dt_clf_gini.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_gini))

# 6. Save model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "wb") as model_file:
    pickle.dump(dt_clf_gini, model_file)
print(f"Model saved to {model_path}")