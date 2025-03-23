# Import packages, modules
import sys
import os
import pandas as pd
from services.data_services import DataServices
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from opcua import Client
from opc_ua_client.config import ClientConfig
from utils.helpers import log_message


def start_client():
    # Initialize the client
    client = Client(ClientConfig.SERVER_URL)

    try:
        # Connect to the server
        client.connect()
        log_message("Client connected to server")

        # Get the root node
        root_node = client.get_root_node()
        log_message(f"Root node is: {root_node}")

        # Browse the server's address space
        objects = root_node.get_child("0:Objects")
        print("Objects node is:", objects)
        
        # Access the simulated data folder
        simulated_folder = objects.get_child(["2:Simulated Data"])
        print("Simulated Data folder is:", simulated_folder)
      
        temperature, pressure, humidity = DataServices.read_variable(simulated_folder)
        print(f"Temperature: {temperature}, Pressure: {pressure}, Humidity: {humidity}")

        
    
    finally:
        # Disconnect from the server
        client.disconnect()
        log_message("Client disconnected")    

if __name__ == "__main__":
    start_client()

