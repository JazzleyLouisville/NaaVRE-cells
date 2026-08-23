
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--hotspot_summary', action='store', type=str, required=True, dest='hotspot_summary')

arg_parser.add_argument('--param_scenario_name', action='store', type=str, required=True, dest='param_scenario_name')

args = arg_parser.parse_args()
print(args)

id = args.id

hotspot_summary = json.loads(args.hotspot_summary)

param_scenario_name = args.param_scenario_name.replace('"','')


if hotspot_summary:
    lines = [
        f"- {item['district']}: {item['hot_hours']} hot hours, "
        f"peak {item['peak_temperature_c']} C ({item['severity']})"
        for item in hotspot_summary
    ]
else:
    lines = ["- No districts crossed the alert threshold"]

alert_report = "Scenario: " + param_scenario_name + "\n" + "\n".join(lines)
print(alert_report)

file_alert_report = open("/tmp/alert_report_" + id + ".json", "w")
file_alert_report.write(json.dumps(alert_report))
file_alert_report.close()
