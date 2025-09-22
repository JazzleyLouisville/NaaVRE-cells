import json

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--digital_twin_state', action='store', type=str, required=True, dest='digital_twin_state')


args = arg_parser.parse_args()
print(args)

id = args.id

digital_twin_state = json.loads(args.digital_twin_state)





json_output = json.dumps(digital_twin_state, indent=2, default=str)
print(json_output)

