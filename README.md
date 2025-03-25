# Ignition Detection Project

## Overview
This project is designed to detect ignition events using OPC UA and Machine Learning model. The data is stored as a csv file for further analysis.

## Configuration
1. All packages are listed inside requirement.txt file. To install required packages, follow the command line:
    "pip install -r requirements.txt"
2. Navigate to child folder, follow the command line
    "cd server"
3. You can activate virtual environment in this step
4. Follow the command lines to run this project
   
   
   SERVER:
   4.1. "python opc_ua_server\main.py"
   4.2. "python opc_ua_client\main.py"
   4.3. "python ml_model\train.py"
   4.2. "python ml_model\predict.py"


   CLIENT
   4.5. "npm start"
