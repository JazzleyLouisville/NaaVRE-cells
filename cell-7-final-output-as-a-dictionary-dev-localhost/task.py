
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--s', action='store', type=int, required=True, dest='s')

arg_parser.add_argument('--xs', action='store', type=str, required=True, dest='xs')

arg_parser.add_argument('--xs2', action='store', type=str, required=True, dest='xs2')

arg_parser.add_argument('--ys', action='store', type=str, required=True, dest='ys')


args = arg_parser.parse_args()
print(args)

id = args.id

s = args.s
xs = json.loads(args.xs)
xs2 = json.loads(args.xs2)
ys = json.loads(args.ys)



output = {
    'original_list': xs,
    'scaled_list': xs2,
    'transformed_list': ys,
    'sum_scaled': s
}
print('Final output:', output)

