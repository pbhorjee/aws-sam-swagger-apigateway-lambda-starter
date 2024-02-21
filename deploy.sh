#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="zaha-crm-api-deployment-workspace-12345"

aws s3 mb s3://$BUCKET

# Uploads files to S3 bucket and creates CloudFormation template
sam package \
    --template-file template.yaml \
    --s3-bucket $BUCKET \
    --output-template-file package.yaml

# Deploys your stack
sam deploy \
    --template-file package.yaml \
    --stack-name zaha-crm-api-stack \
    --capabilities CAPABILITY_IAM
