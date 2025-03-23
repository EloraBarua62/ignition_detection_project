# Import libraries
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from preprocessing.preprocess import preprocess_data

def train_model():
    # Load Dataset
    file_path = r"H:\Personal Projects\OPC UA\opcua_ml_project\ml_model\data\sensor_data.csv"
    df = pd.read_csv(file_path)

    # Preprocess data
    df = preprocess_data(df)

    # Split dataset
    X = df[["Temperature", "Pressure", "Humidity"]]
    y = df["Failure"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Model Accuracy: {accuracy:.2f}")

    # Ensure the models directory exists
    os.makedirs("ml_model/models", exist_ok=True)
    
    # Save model
    joblib.dump(model, "ml_model/models/failure_predictor.pkl")
    print("Model saved as failure_predictor.pkl")

if __name__ == "__main__":
    train_model()