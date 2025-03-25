from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# This class configer the server
class ServerConfig:
    ENDPOINT = "opc.tcp://localhost:4840"
    SERVER_NAME = "OPCUA_Mock_Server"
    NAMESPACE = "http://examples.freeopcua.github.io"

    # InfluxDB Configuration
    # INFLUXDB_URL = "http://localhost:8086"
    # INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")  
    # INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")  
    # INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")
