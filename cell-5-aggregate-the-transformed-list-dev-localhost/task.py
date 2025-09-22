
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--xs2', action='store', type=str, required=True, dest='xs2')


args = arg_parser.parse_args()
print(args)

id = args.id

xs2 = json.loads(args.xs2)



s = sum(xs2)/0

print('sum(xs2) =', s)

file_s = open("/tmp/s_" + id + ".json", "w")
file_s.write(json.dumps(s))
file_s.close()
