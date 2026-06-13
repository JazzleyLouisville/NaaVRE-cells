import pandas as pd
import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--raw_point_cloud', action='store', type=str, required=True, dest='raw_point_cloud')


args = arg_parser.parse_args()
print(args)

id = args.id

raw_point_cloud = json.loads(args.raw_point_cloud)



df = pd.DataFrame(np.random.rand(100, 4), columns=['x', 'y', 'z', 'intensity'])

processed_data = filter_point_cloud(df, threshold=0.2)
print('Preprocessing complete.')

file_processed_point_cloud = open("/tmp/processed_point_cloud_" + id + ".json", "w")
file_processed_point_cloud.write(json.dumps(processed_point_cloud))
file_processed_point_cloud.close()
