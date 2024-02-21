import base64
import boto3
import json
import random

s3 = boto3.client("s3")

def handler(event, context):
    number = random.randint(0,2)
    
    if number == 0:
        return {
            "isBase64Encoded": False,
            "headers": { "Content-type": "application/json" },
            "statusCode": 200,
            "body": json.dumps({ "RESULT": [
                {
                    "id": "3453545345",
                    "status": "submitted"
                }
            ]})
        }
    elif number == 1:
        return {
            "isBase64Encoded": False,
            "headers": { "Content-type": "application/json" },
            "statusCode": 200,
            "body": json.dumps({ "RESULT": [
                {
                    "id": "3453545345",
                    "status": "processing"
                }
            ]})
        }
    else:
        return {
            "isBase64Encoded": False,
            "headers": { "Content-type": "application/json" },
            "statusCode": 200,
            "body": json.dumps({ "RESULT": [
                {
                    "id": "3453545345",
                    "status": "completed"
                }
            ]})
        }
