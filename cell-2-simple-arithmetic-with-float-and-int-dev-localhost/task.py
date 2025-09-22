
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a', action='store', type=float, required=True, dest='a')

arg_parser.add_argument('--n', action='store', type=int, required=True, dest='n')


args = arg_parser.parse_args()
print(args)

id = args.id

a = args.a
n = args.n



b = a * n
print('b = a * n =', b)

