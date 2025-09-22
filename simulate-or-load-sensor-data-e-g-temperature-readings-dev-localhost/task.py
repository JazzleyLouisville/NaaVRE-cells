import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




np.random.seed(42)

plt.rcParams['figure.figsize'] = (10, 5)

time_index = pd.date_range(start='2025-01-01', periods=100, freq='H')
sensor_data = pd.DataFrame({
    'temperature': 20 + 5 * np.sin(np.linspace(0, 20, 100)) + np.random.normal(0, 0.5, 100),
    'humidity': 50 + 10 * np.random.randn(100)
}, index=time_index)

json_data = sensor_data.to_json(orient='records', date_format='iso')

file_json_data = open("/tmp/json_data_" + id + ".json", "w")
file_json_data.write(json.dumps(json_data))
file_json_data.close()
