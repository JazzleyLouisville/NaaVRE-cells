
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




a = 3.14  # float
n = 7     # int
xs = [1, 2, 3]  # list of ints
print('a =', a)
print('n =', n)
print('xs =', xs)

file_a = open("/tmp/a_" + id + ".json", "w")
file_a.write(json.dumps(a))
file_a.close()
file_n = open("/tmp/n_" + id + ".json", "w")
file_n.write(json.dumps(n))
file_n.close()
file_xs = open("/tmp/xs_" + id + ".json", "w")
file_xs.write(json.dumps(xs))
file_xs.close()
