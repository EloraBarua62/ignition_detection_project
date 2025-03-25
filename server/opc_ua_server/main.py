# Import packages
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
import time
from opcua import Server, ua
from config import ServerConfig
from opc_ua_server.models.methods import multiply
from utils.helpers import log_message
from opc_ua_server.models.nodes import create_address_space
# from influxdb_client import InfluxDBClient, Point
# from influxdb_client.client.write_api import SYNCHRONOUS



# Initialize InfluxDB Client
# influx_client = InfluxDBClient(
#     url=ServerConfig.INFLUXDB_URL,
#     token=ServerConfig.INFLUXDB_TOKEN,
#     org=ServerConfig.INFLUXDB_ORG
# )
# write_api = influx_client.write_api(write_options=SYNCHRONOUS)




# Method: Project setup , then start the server
def start_server():
    # Initialize the server
    # This will create an instance of the server
    server = Server()
    server.set_endpoint(ServerConfig.ENDPOINT)
    server.set_server_name(ServerConfig.SERVER_NAME)

    # Register a namespace
    index = server.register_namespace(ServerConfig.NAMESPACE)

    # Create address space
    my_object, temperature, pressure, humidity = create_address_space(server, index)

    # Add a custom method
    result = my_object.add_method(index, "Multiply", multiply, [ua.VariantType.Int32], [ua.VariantType.Int32])
    log_message(f"Multiplication: {result}")

    # Start the server
    server.start()
    log_message(f"Server is running at {ServerConfig.ENDPOINT}")
  

    try:
        while True:
            # Generate random values for temperature, pressure, and humidity
            temp_value = round(random.uniform(20.0, 50.0), 2)
            pressure_value = round(random.uniform(100.0, 110.0), 2)
            humidity_value = round(random.uniform(50.0, 70.0), 2)

            # Update the OPC UA variables
            temperature.set_value(temp_value)
            pressure.set_value(pressure_value)
            humidity.set_value(humidity_value)

            print(f"Updated Values - Temperature: {temp_value}, Pressure: {pressure_value}, Humidity: {humidity_value}")


            # # Write data to InfluxDB
            # point = Point("sensor_data") \
            #     .field("temperature", temp_value) \
            #     .field("pressure", pressure_value) \
            #     .field("humidity", humidity_value)
            # write_api.write(bucket=ServerConfig.INFLUXDB_BUCKET, record=point)
            # log_message("Data written to InfluxDB.")



            # Wait for 2 seconds before the next update
            time.sleep(2)
    except KeyboardInterrupt:
        server.stop()
        log_message("Server stopped.")

    
# Main access point for the server
if __name__ == "__main__":
    # Project setup , then start the server
    start_server()