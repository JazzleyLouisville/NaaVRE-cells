from datetime import datetime
import random
import time

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--split_data', action='store', type=str, required=True, dest='split_data')


args = arg_parser.parse_args()
print(args)

id = args.id

split_data = json.loads(args.split_data)




processed_results = []

def apply_digital_twin_model(sensor_group):
    """
    Apply appropriate digital twin model based on sensor type
    
    Args:
        sensor_group: Group of sensor readings of the same type
        
    Returns:
        Processed sensor data with predictions and health scores
    """
    sensor_type = sensor_group[0]['sensor_type']
    processed_group = []
    
    print(f"Processing {len(sensor_group)} {sensor_type} readings...")
    time.sleep(1)  # Simulate processing time
    
    for data_point in sensor_group:
        processed_point = data_point.copy()
        
        if sensor_type == 'temperature':
            processed_point['predicted_value'] = data_point['value'] + random.uniform(-0.5, 1.5)
            processed_point['health_score'] = min(100, max(0, 100 - abs(data_point['value'] - 25) * 5))
            
        elif sensor_type == 'pressure':
            processed_point['predicted_value'] = data_point['value'] * random.uniform(0.95, 1.05)
            processed_point['health_score'] = min(100, max(0, 100 - abs(data_point['value'] - 1013) / 5))
            
        elif sensor_type == 'humidity':
            processed_point['predicted_value'] = data_point['value'] + random.uniform(-2, 2)
            processed_point['health_score'] = min(100, max(0, 100 - abs(data_point['value'] - 45) * 2))
            
        elif sensor_type == 'vibration':
            processed_point['predicted_value'] = data_point['value'] * random.uniform(0.9, 1.1)
            processed_point['health_score'] = min(100, max(0, 100 - (data_point['value'] * 100)))
            
        else:  # voltage or other
            processed_point['predicted_value'] = data_point['value'] + random.uniform(-5, 5)
            processed_point['health_score'] = min(100, max(0, 100 - abs(data_point['value'] - 220) / 2))
        
        processed_point['health_score'] = round(processed_point['health_score'], 1)
        processed_point['predicted_value'] = round(processed_point['predicted_value'], 2)
        processed_group.append(processed_point)
    
    return {
        "sensor_type": sensor_type,
        "data": processed_group,
        "average_health": round(sum(p['health_score'] for p in processed_group) / len(processed_group), 1),
        "timestamp": datetime.now().isoformat()
    }

for group in split_data:
    result = apply_digital_twin_model(group)
    processed_results.append(result)

print(f"\nProcessed {len(processed_results)} sensor groups")
for result in processed_results:
    print(f"{result['sensor_type']}: Average health score = {result['average_health']}")

file_processed_results = open("/tmp/processed_results_" + id + ".json", "w")
file_processed_results.write(json.dumps(processed_results))
file_processed_results.close()
