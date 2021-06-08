import json

# import requests


def get_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

def post_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "post world",
            # "location": ip.text.replace("\n", "")
        }),
    }
