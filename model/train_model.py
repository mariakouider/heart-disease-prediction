# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data_path = 'model/heart.csv'
data = pd.read_csv(data_path)

# Separate features and target
X = data.drop("target", axis=1)
y = data["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# Save the model to the 'model' directory
model_path = 'model/rf_model.pkl'
with open(model_path, 'wb') as file:
    pickle.dump(rf_model, file)

print("Random Forest model has been trained and saved successfully!")
