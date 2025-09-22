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

sensor_data.head()
print(type(sensor_data.head()))

file_sensor_data = open("/tmp/sensor_data_" + id + ".json", "w")
file_sensor_data.write(json.dumps(sensor_data))
file_sensor_data.close()
