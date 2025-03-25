import sys
import os
from dotenv import load_dotenv
import time
import joblib
import json
import numpy as np
from opcua import Client as OPCUAClient
from services.data_services import DataServices
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from ml_model.config import ClientConfig   
from utils.helpers import log_message
import paho.mqtt.client as MQTTClient  


load_dotenv()


# MQTT_BROKER="88bc31db9f754bb9bca79160194b48dd.s1.eu.hivemq.cloud"  
# MQTT_PORT=8883
# MQTT_TOPIC="opcua/ml_predictions"
# MQTT_USER="elora_barua"  
# MQTT_PASS="Elora62Barua"

# mqtt_client = MQTTClient.Client()
# mqtt_client.username_pw_set(MQTT_USER, MQTT_PASS)
# mqtt_client.tls_set() 
# mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

def predict_failure():
    # Load the model 
    model = joblib.load("ml_model/models/failure_predictor.pkl")

    # Initialize the client
    opcua_client = OPCUAClient(ClientConfig.SERVER_URL)

    # Connect to the server
    opcua_client.connect()
    log_message("Client connected to server")

    # Get the root node
    root_node = opcua_client.get_root_node()

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


            # # # Prepare JSON payload
            # prediction_data = {
            #     "temperature": temp,
            #     "pressure": pres,
            #     "humidity": humd,
            #     "prediction": prediction
            # }

            # # # Publish to MQTT topic
            # mqtt_client.publish(os.getenv("MQTT_TOPIC"), json.dumps(prediction_data))

            # print("Published:", prediction_data)
            time.sleep(2)
    except KeyboardInterrupt:
        log_message("\nStopping client...")
        opcua_client.disconnect()


if __name__ == "__main__":
    predict_failure()