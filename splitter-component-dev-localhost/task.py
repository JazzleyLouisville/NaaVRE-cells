import json

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--data_groups', action='store', type=str, required=True, dest='data_groups')


args = arg_parser.parse_args()
print(args)

id = args.id

data_groups = json.loads(args.data_groups)




def splitter(data_array):
    """
    Simulates the Splitter component functionality
    
    Args:
        data_array: Array to be split into individual elements
        
    Returns:
        The same array (in a real Splitter, this would trigger parallel execution)
    """
    print(f"Splitter: Splitting array with {len(data_array)} elements for parallel processing")
    return data_array

split_data = splitter(data_groups)

print("Each group will now be processed in parallel in the next cell")

print("\nFirst group preview:")
print(json.dumps(split_data[0][0], indent=2))

file_split_data = open("/tmp/split_data_" + id + ".json", "w")
file_split_data.write(json.dumps(split_data))
file_split_data.close()
