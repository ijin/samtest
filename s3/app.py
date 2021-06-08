import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['detail']['resources'][1]['ARN'].split(":")[-1]
    try:
        response = s3.get_bucket_location(Bucket=bucket)
        print(response)
        return response
    except Exception as e:
        print(e)
        raise e
