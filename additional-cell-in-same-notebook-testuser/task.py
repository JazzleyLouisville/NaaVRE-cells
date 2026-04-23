
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--processed_data', action='store', type=str, required=True, dest='processed_data')


args = arg_parser.parse_args()
print(args)

id = args.id

processed_data = args.processed_data.replace('"','')



print(processed_data)

