import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score
import pandas as pd
import joblib

# Load the dataset
data_path = "data/heart.csv"
data = pd.read_csv(data_path)

# Prepare data
X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Random Forest Model with Hyperparameter Tuning
rf_param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5, 10],
}

rf_grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid=rf_param_grid,
    scoring="roc_auc",
    cv=5,
)
rf_grid.fit(X_train, y_train)
rf_best_model = rf_grid.best_estimator_

# Evaluate the model
rf_predictions = rf_best_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
rf_roc_auc = roc_auc_score(y_test, rf_best_model.predict_proba(X_test)[:, 1])

print("Model Evaluation:")
print(f"Accuracy: {rf_accuracy:.2f}")
print(f"ROC AUC: {rf_roc_auc:.2f}")

import joblib
from sklearn.ensemble import RandomForestClassifier

# Save the trained model
model_path = "rf_model.pkl"
joblib.dump(rf_best_model, model_path)
print(f"Model saved to {model_path}")

# Test loading the model
loaded_model = joblib.load(model_path)
print("Model loaded successfully")

