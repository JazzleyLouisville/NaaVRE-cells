import pandas as pd
import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--filter_point_cloud', action='store', type=None, required=True, dest='filter_point_cloud')

arg_parser.add_argument('--np', action='store', type=None, required=True, dest='np')

arg_parser.add_argument('--pd', action='store', type=None, required=True, dest='pd')


args = arg_parser.parse_args()
print(args)

id = args.id

filter_point_cloud = args.filter_point_cloud
np = args.np
pd = args.pd



df = pd.DataFrame(np.random.rand(100, 4), columns=['x', 'y', 'z', 'intensity'])

processed_data = filter_point_cloud(df, threshold=0.5)
print('Preprocessing complete.')

