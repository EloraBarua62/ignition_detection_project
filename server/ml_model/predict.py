import sys
import os
import time
import joblib
import numpy as np
from opcua import Client
from services.data_services import DataServices
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from ml_model.config import ClientConfig
from utils.helpers import log_message


def predict_failure():
    # Load the model 
    model = joblib.load("ml_model/models/failure_predictor.pkl")

    # Initialize the client
    client = Client(ClientConfig.SERVER_URL)

    # Connect to the server
    client.connect()
    log_message("Client connected to server")

    # Get the root node
    root_node = client.get_root_node()

    # Browse the server's address space
    objects = root_node.get_child("0:Objects")
    
    # Access the simulated data folder
    simulated_folder = objects.get_child(["2:Simulated Data"])

    try:
        while True:
            # Store data into dataframe
            temp, pres, humd = DataServices.read_variable(simulated_folder)
            # Define feature names exactly as used during training
            feature_names = ["Temperature", "Pressure", "Humidity"]

            # Convert the input array to a DataFrame with column names
            X_test = pd.DataFrame([[temp, pres, humd]], columns=feature_names)
            prediction = model.predict(X_test)[0]
            status = " Machine Failure Risk!" if prediction == 1 else "Machine Running Normally"

            print(f"Temperature: {temp:.2f} °C | pressure: {pres:.2f}| humidity: {humd}| status → {status}")
            time.sleep(2)
    except KeyboardInterrupt:
        log_message("\nStopping client...")
        client.disconnect()


if __name__ == "__main__":
    predict_failure()