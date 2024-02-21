import base64
import boto3

s3 = boto3.client("s3")

def handler(event, context):
    response = s3.get_object(
        Bucket="zaha-crm-api-deployment-workspace-12345",
        Key="test.csv.zip",
    )
    
    zip = response["Body"].read()
    
    return {
        "headers": { 
            "Content-Type": "application/zip",
            "Content-Disposition": "inline"
        },
        "statusCode": 200,
        "body": base64.b64encode(zip).decode("utf-8"),
        "isBase64Encoded": True
    }