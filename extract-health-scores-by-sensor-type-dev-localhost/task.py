import matplotlib.pyplot as plt
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--merged_results', action='store', type=str, required=True, dest='merged_results')


args = arg_parser.parse_args()
print(args)

id = args.id

merged_results = json.loads(args.merged_results)



sensor_types = []
health_scores = []

for result in merged_results['merged_results']:
    sensor_types.append(result['sensor_type'])
    health_scores.append(result['average_health'])

plt.figure(figsize=(10, 6))
bars = plt.bar(sensor_types, health_scores, color=['#3498db', '#2ecc71', '#e74c3c', '#f1c40f', '#9b59b6'])
plt.ylim(0, 100)
plt.title('Digital Twin: Average Health Score by Sensor Type')
plt.xlabel('Sensor Type')
plt.ylabel('Average Health Score (%)')
plt.axhline(y=70, color='r', linestyle='--', alpha=0.7, label='Critical Threshold')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}%', ha='center', va='bottom')

plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()

all_processed_data = []
for result in merged_results['merged_results']:
    for data_point in result['data']:
        all_processed_data.append(data_point)

df = pd.DataFrame(all_processed_data)

print("Summary of processed sensor data:")
df

