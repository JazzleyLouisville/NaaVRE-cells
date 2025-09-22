import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--json_data', action='store', type=str, required=True, dest='json_data')


args = arg_parser.parse_args()
print(args)

id = args.id

json_data = json.loads(args.json_data)




cleaned_data = pd.read_json(json_data, orient='records')
cleaned_data = cleaned_data[(cleaned_data['humidity'] >= 20) & (cleaned_data['humidity'] <= 80)]

cleaned_data = cleaned_data.fillna(method='ffill')

cleaned_data['temperature_norm'] = (cleaned_data['temperature'] - cleaned_data['temperature'].mean()) / cleaned_data['temperature'].std()
cleaned_json_data = cleaned_data.to_json(orient='records', date_format='iso')

file_cleaned_json_data = open("/tmp/cleaned_json_data_" + id + ".json", "w")
file_cleaned_json_data.write(json.dumps(cleaned_json_data))
file_cleaned_json_data.close()
