from collections import defaultdict

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--city_readings', action='store', type=str, required=True, dest='city_readings')

arg_parser.add_argument('--param_min_hot_hours', action='store', type=int, required=True, dest='param_min_hot_hours')
arg_parser.add_argument('--param_threshold_c', action='store', type=float, required=True, dest='param_threshold_c')

args = arg_parser.parse_args()
print(args)

id = args.id

city_readings = json.loads(args.city_readings)

param_min_hot_hours = args.param_min_hot_hours
param_threshold_c = args.param_threshold_c


severity = "warning"
hot_hours = defaultdict(list)
for reading in city_readings:
    if reading["temperature_c"] >= param_threshold_c:
        hot_hours[reading["district"]].append(reading)

hotspot_summary = []
for district, readings in sorted(hot_hours.items()):
    if len(readings) >= param_min_hot_hours:
        hotspot_summary.append({
            "district": district,
            "severity": severity,
            "hot_hours": len(readings),
            "peak_temperature_c": max(item["temperature_c"] for item in readings),
        })

print(f"Detected {len(hotspot_summary)} hotspots at or above {param_threshold_c} C")

file_hotspot_summary = open("/tmp/hotspot_summary_" + id + ".json", "w")
file_hotspot_summary.write(json.dumps(hotspot_summary))
file_hotspot_summary.close()
