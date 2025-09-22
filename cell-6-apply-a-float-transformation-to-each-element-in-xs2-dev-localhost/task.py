
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=float, required=True, dest='a')

arg_parser.add_argument('--xs2', action='store', type=str, required=True, dest='xs2')


args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a
xs2 = json.loads(args.xs2)



ys = [x / a for x in xs2]
print('ys =', ys)

file_ys = open("/tmp/ys_" + id + ".json", "w")
file_ys.write(json.dumps(ys))
file_ys.close()
