
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




numbers = ["x","y","z","a","q"]

file_numbers = open("/tmp/numbers_" + id + ".json", "w")
file_numbers.write(json.dumps(numbers))
file_numbers.close()
