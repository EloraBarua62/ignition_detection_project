def create_address_space(server, addspace):
    # Get the objects node
    objects = server.get_objects_node()

    # Add a new folder for simulated data
    simulated_data = objects.add_folder(addspace, "Simulated Data")

    # Add variables to the folder
    temperature = simulated_data.add_variable(addspace, "Temperature", 0.0)
    pressure = simulated_data.add_variable(addspace, "Pressure", 0.0)
    humidity = simulated_data.add_variable(addspace, "Humidity", 0.0)

    # Set variables as writable 
    temperature.set_writable()
    pressure.set_writable()
    humidity.set_writable()

    return simulated_data, temperature, pressure, humidity
