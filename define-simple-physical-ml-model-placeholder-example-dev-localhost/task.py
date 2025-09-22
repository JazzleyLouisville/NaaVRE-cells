from io import StringIO
import numpy as np
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--cleaned_json_data', action='store', type=None, required=True, dest='cleaned_json_data')


args = arg_parser.parse_args()
print(args)

id = args.id

cleaned_json_data = args.cleaned_json_data



cleaned_data = pd.read_json(StringIO(cleaned_json_data), orient='records')

def simple_temperature_model(t, base=20, amplitude=5, noise_level=0.5):
    return base + amplitude * np.sin(t) + np.random.normal(0, noise_level, len(t))

t = np.linspace(0, 20, len(cleaned_data))
model_output = simple_temperature_model(t) #numpy arrays cannot be passed as JSON objects we need to fix this
model_output_list = list(model_output)

file_model_output_list = open("/tmp/model_output_list_" + id + ".json", "w")
file_model_output_list.write(json.dumps(model_output_list))
file_model_output_list.close()
