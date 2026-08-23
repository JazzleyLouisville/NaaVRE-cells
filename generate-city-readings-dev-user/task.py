import random
import math

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_hours', action='store', type=int, required=True, dest='param_hours')
arg_parser.add_argument('--param_seed', action='store', type=int, required=True, dest='param_seed')

args = arg_parser.parse_args()
print(args)

id = args.id


param_hours = args.param_hours
param_seed = args.param_seed


rng = random.Random(param_seed)
districts = ["Centrum", "West", "Nieuw-West", "Oost"]
city_readings = []
for hour in range(param_hours):
    daily_curve = 6.5 * math.sin((hour - 7) * math.pi / 12)
    for district_index, district in enumerate(districts):
        urban_heat = district_index * 0.7
        temperature_c = 26.0 + daily_curve + urban_heat + rng.uniform(-0.6, 0.6)
        city_readings.append({
            "district": district,
            "hour": hour,
            "temperature_c": round(temperature_c, 1),
        })

print(f"Generated {len(city_readings)} readings across {len(districts)} districts")

file_city_readings = open("/tmp/city_readings_" + id + ".json", "w")
file_city_readings.write(json.dumps(city_readings))
file_city_readings.close()
