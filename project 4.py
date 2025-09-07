# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load dataset (example: Iris dataset)
from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Choose model
model = LogisticRegression(max_iter=200)

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))
