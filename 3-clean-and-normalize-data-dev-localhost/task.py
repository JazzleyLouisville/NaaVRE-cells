
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--sensor_data', action='store', type=float, required=True, dest='sensor_data')


args = arg_parser.parse_args()
print(args)

id = args.id

sensor_data = args.sensor_data



cleaned_data = sensor_data.copy()

cleaned_data = cleaned_data[(cleaned_data['humidity'] >= 20) & (cleaned_data['humidity'] <= 80)]

cleaned_data = cleaned_data.fillna(method='ffill')

cleaned_data['temperature_norm'] = (cleaned_data['temperature'] - cleaned_data['temperature'].mean()) / cleaned_data['temperature'].std()

cleaned_data.head()

file_cleaned_data = open("/tmp/cleaned_data_" + id + ".json", "w")
file_cleaned_data.write(json.dumps(cleaned_data))
file_cleaned_data.close()
