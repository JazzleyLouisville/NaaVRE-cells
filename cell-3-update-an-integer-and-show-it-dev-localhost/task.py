
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--n', action='store', type=int, required=True, dest='n')


args = arg_parser.parse_args()
print(args)

id = args.id

n = args.n



n2 = n + 5
print('n2 = n + 5 =', n2)

file_n2 = open("/tmp/n2_" + id + ".json", "w")
file_n2.write(json.dumps(n2))
file_n2.close()
