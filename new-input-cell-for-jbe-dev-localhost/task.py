
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




numbers = ["x","y","z","a"]
followers = [1,2,3,4,5]

file_numbers = open("/tmp/numbers_" + id + ".json", "w")
file_numbers.write(json.dumps(numbers))
file_numbers.close()
file_followers = open("/tmp/followers_" + id + ".json", "w")
file_followers.write(json.dumps(followers))
file_followers.close()
