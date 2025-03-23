# Import libraries
import time

data = []

class DataServices:
    @staticmethod
    def read_variable(simulated_folder): 
        # Access the temperature, pressure, and humidity nodes
        temperature = simulated_folder.get_child(["2:Temperature"])
        pressure = simulated_folder.get_child(["2:Pressure"])
        humidity = simulated_folder.get_child(["2:Humidity"])        
        return temperature, pressure, humidity
    
    @staticmethod
    def write_variable(client, node_id, value):
        node = client.get_node(node_id)
        node.set_value(value)
        print(f"Variable updated to: {value}")