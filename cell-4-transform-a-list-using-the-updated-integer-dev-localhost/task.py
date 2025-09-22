
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--n2', action='store', type=int, required=True, dest='n2')

arg_parser.add_argument('--xs', action='store', type=str, required=True, dest='xs')

arg_parser.add_argument('--xsq', action='store', type=int, required=True, dest='xsq')


args = arg_parser.parse_args()
print(args)

id = args.id

n2 = args.n2
xs = json.loads(args.xs)
xsq = args.xsq



xs2 = [x * n2 for x in xs]
print('xs2 =', xsq)

file_xs2 = open("/tmp/xs2_" + id + ".json", "w")
file_xs2.write(json.dumps(xs2))
file_xs2.close()
