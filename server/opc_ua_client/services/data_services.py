# Import libraries
import time

data = []

class DataServices:
    @staticmethod
    def read_variable(simulated_folder): 
        # Access the temperature, pressure, and humidity nodes
        temperature_node = simulated_folder.get_child(["2:Temperature"])
        pressure_node = simulated_folder.get_child(["2:Pressure"])
        humidity_node = simulated_folder.get_child(["2:Humidity"])  

        for _ in range(50):
            # Read the values
            temperature = temperature_node.get_value()
            pressure = pressure_node.get_value()
            humidity = humidity_node.get_value()
            print(f"Temperature: {temperature}, Pressure: {pressure}, Humidity: {humidity}")
            data.append([temperature, pressure, humidity])
            time.sleep(2)        
        return data
    
    @staticmethod
    def write_variable(client, node_id, value):
        node = client.get_node(node_id)
        node.set_value(value)
        print(f"Variable updated to: {value}")