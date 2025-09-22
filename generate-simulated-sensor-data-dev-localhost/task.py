from datetime import datetime
import pandas as pd
import random
from datetime import timedelta

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id





def generate_sensor_data(num_sensors=5, num_readings=10):
    """
    Generate simulated sensor data for multiple sensors
    
    Args:
        num_sensors: Number of sensors to simulate
        num_readings: Number of readings per sensor
        
    Returns:
        List of dictionaries with sensor data
    """
    sensor_types = ['temperature', 'pressure', 'humidity', 'vibration', 'voltage']
    base_values = {'temperature': 25.0, 'pressure': 1013.0, 'humidity': 50.0, 'vibration': 0.5, 'voltage': 220.0}
    variation = {'temperature': 5.0, 'pressure': 50.0, 'humidity': 20.0, 'vibration': 0.3, 'voltage': 10.0}
    units = {'temperature': '°C', 'pressure': 'hPa', 'humidity': '%', 'vibration': 'mm/s', 'voltage': 'V'}
    
    start_time = datetime.now()
    
    all_sensor_data = []
    
    for i in range(num_sensors):
        sensor_id = f"sensor_{i+1}"
        sensor_type = sensor_types[i % len(sensor_types)]
        base_value = base_values[sensor_type]
        var = variation[sensor_type]
        unit = units[sensor_type]
        
        for j in range(num_readings):
            timestamp = start_time + timedelta(minutes=j*5)
            value = base_value + (random.random() * 2 - 1) * var
            
            data_point = {
                "sensor_id": sensor_id,
                "sensor_type": sensor_type,
                "timestamp": timestamp.isoformat(),
                "value": round(value, 2),
                "unit": unit
            }
            all_sensor_data.append(data_point)
    
    return all_sensor_data

sensor_data = generate_sensor_data(num_sensors=5, num_readings=4)

print(f"Generated {len(sensor_data)} sensor readings")
pd.DataFrame(sensor_data).head(10)

file_sensor_data = open("/tmp/sensor_data_" + id + ".json", "w")
file_sensor_data.write(json.dumps(sensor_data))
file_sensor_data.close()
