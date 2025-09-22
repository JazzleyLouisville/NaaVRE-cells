from io import StringIO
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--cleaned_json_data', action='store', type=str, required=True, dest='cleaned_json_data')

arg_parser.add_argument('--json_data_simulation_df', action='store', type=str, required=True, dest='json_data_simulation_df')


args = arg_parser.parse_args()
print(args)

id = args.id

cleaned_json_data = json.loads(args.cleaned_json_data)
json_data_simulation_df = json.loads(args.json_data_simulation_df)



cleaned_data = pd.read_json(StringIO(cleaned_json_data), orient='records')
simulation_df = pd.read_json(StringIO(json_data_simulation_df),orient='records')
latest_real = cleaned_data.iloc[-1]
latest_sim = simulation_df.iloc[-1]

digital_twin_state = {
    'timestamp': latest_real.name,
    'real_temperature': latest_real['temperature'],
    'simulated_temperature': latest_sim['simulated_temperature'],
    'delta': latest_real['temperature'] - latest_sim['simulated_temperature']
}

digital_twin_state

file_digital_twin_state = open("/tmp/digital_twin_state_" + id + ".json", "w")
file_digital_twin_state.write(json.dumps(digital_twin_state))
file_digital_twin_state.close()
