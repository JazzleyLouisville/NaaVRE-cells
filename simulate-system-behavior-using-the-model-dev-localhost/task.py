from io import StringIO
import numpy as np
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--cleaned_json_data', action='store', type=str, required=True, dest='cleaned_json_data')

arg_parser.add_argument('--model_output_list', action='store', type=str, required=True, dest='model_output_list')


args = arg_parser.parse_args()
print(args)

id = args.id

cleaned_json_data = json.loads(args.cleaned_json_data)
model_output_list = json.loads(args.model_output_list)




cleaned_data = pd.read_json(StringIO(cleaned_json_data), orient='records')
model_output = np.array(model_output_list)
t = np.linspace(0, 20, len(cleaned_data))

simulation_df = pd.DataFrame({
    'timestamp': cleaned_data.index,
    'simulated_temperature': model_output
}).set_index('timestamp')


json_data_simulation_df = simulation_df.head().to_json(orient='records', date_format='iso')

file_json_data_simulation_df = open("/tmp/json_data_simulation_df_" + id + ".json", "w")
file_json_data_simulation_df.write(json.dumps(json_data_simulation_df))
file_json_data_simulation_df.close()
