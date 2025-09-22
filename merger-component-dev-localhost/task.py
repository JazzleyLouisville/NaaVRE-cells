from datetime import datetime

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--processed_results', action='store', type=str, required=True, dest='processed_results')


args = arg_parser.parse_args()
print(args)

id = args.id

processed_results = json.loads(args.processed_results)




def merger(results_array):
    """
    Simulates the Merger component functionality
    
    Args:
        results_array: Array of results from parallel executions
        
    Returns:
        Merged result
    """
    print(f"Merger: Combining {len(results_array)} results from parallel processing")
    return {
        "merged_results": results_array,
        "total_readings": sum(len(result['data']) for result in results_array),
        "timestamp": datetime.now().isoformat()
    }

merged_results = merger(processed_results)

print(f"Merged {merged_results['total_readings']} total readings from {len(merged_results['merged_results'])} sensor types")
print(f"Merged data timestamp: {merged_results['timestamp']}")

file_merged_results = open("/tmp/merged_results_" + id + ".json", "w")
file_merged_results.write(json.dumps(merged_results))
file_merged_results.close()
