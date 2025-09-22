
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--sensor_data', action='store', type=str, required=True, dest='sensor_data')


args = arg_parser.parse_args()
print(args)

id = args.id

sensor_data = json.loads(args.sensor_data)



def group_by_sensor_type(sensor_data):
    """
    Group sensor data by sensor type
    
    Args:
        sensor_data: List of sensor data points
        
    Returns:
        Dictionary with sensor types as keys and lists of data points as values
    """
    grouped_data = {}
    
    for data_point in sensor_data:
        sensor_type = data_point['sensor_type']
        if sensor_type not in grouped_data:
            grouped_data[sensor_type] = []
        grouped_data[sensor_type].append(data_point)
    
    return grouped_data

grouped_sensor_data = group_by_sensor_type(sensor_data)

data_groups = list(grouped_sensor_data.values())

print(f"Created {len(data_groups)} data groups for parallel processing:")
for i, group in enumerate(data_groups):
    print(f"Group {i+1}: {group[0]['sensor_type']} - {len(group)} readings")

file_data_groups = open("/tmp/data_groups_" + id + ".json", "w")
file_data_groups.write(json.dumps(data_groups))
file_data_groups.close()
