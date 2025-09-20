
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_copernicus_password_general_user_account = os.getenv('secret_copernicus_password_general_user_account')
secret_s3_access_key = os.getenv('secret_s3_access_key')
secret_s3_secret_key = os.getenv('secret_s3_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--acolite_processing', action='store', type=str, required=True, dest='acolite_processing')

arg_parser.add_argument('--param_copernicus_e_mail_general_user_account', action='store', type=str, required=True, dest='param_copernicus_e_mail_general_user_account')
arg_parser.add_argument('--param_s3_public_bucket', action='store', type=str, required=True, dest='param_s3_public_bucket')
arg_parser.add_argument('--param_s3_server', action='store', type=str, required=True, dest='param_s3_server')
arg_parser.add_argument('--year', action='store', type=int, required=True, dest='year')

args = arg_parser.parse_args()
print(args)

id = args.id

acolite_processing = json.loads(args.acolite_processing)

param_copernicus_e_mail_general_user_account = args.param_copernicus_e_mail_general_user_account.replace('"','')
param_s3_public_bucket = args.param_s3_public_bucket.replace('"','')
param_s3_server = args.param_s3_server.replace('"','')
year = args.year



acolite_processing

