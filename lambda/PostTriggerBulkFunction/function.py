import json

def handler(event, context):
    return {
            "isBase64Encoded": False,
            "headers": { "Content-type": "application/json" },
            "statusCode": 200,
            "body": json.dumps({ "RESULT": [
                {
                    "id": "3453545345"
                }
            ]})
        }