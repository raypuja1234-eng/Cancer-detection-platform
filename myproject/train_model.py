"""
train_model.py - Run this script ONCE to train the cancer detection model and save it.
Usage: python train_model.py  (from the myproject/ directory)
"""

import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset — path relative to where this script is run (myproject/)
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cancer_data.csv')

print(f"Loading data from: {os.path.abspath(DATA_PATH)}")
data = pd.read_csv(DATA_PATH)

# Use the same columns as in the notebook: iloc[:, 1:4] → diagnosis, radius_mean, texture_mean
data_final = data.iloc[:, 1:4]
print(f"Columns used: {list(data_final.columns)}")
print(f"Shape: {data_final.shape}")

# Features and target
x = data_final.iloc[:, 1:].values   # radius_mean, texture_mean
y = data_final.iloc[:, 0].values    # diagnosis (M/B)

print(f"Feature shape: {x.shape}, Target classes: {set(y)}")

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Train SVM (same as notebook)
svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(x_train, y_train)

# Evaluate
preds = svm_model.predict(x_test)
acc = accuracy_score(y_test, preds)
print(f"\n[OK] Model trained successfully! Accuracy: {acc:.4f} ({acc*100:.2f}%)")

# Save the model
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cancer_model.pkl')
joblib.dump(svm_model, MODEL_PATH)
print(f"[OK] Model saved to: {MODEL_PATH}")
