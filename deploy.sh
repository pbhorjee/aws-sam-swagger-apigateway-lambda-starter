#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="zaha-crm-api-deployment-workspace-12345"

# Uploads files to S3 bucket and creates CloudFormation template
sam package \
    --template-file template.yaml \
    --s3-bucket zaha-crm-api-deployment-workspace-12345 \
    --output-template-file package.yaml

# Deploys your stack
sam deploy \
    --template-file package.yaml \
    --stack-name zaha-crm-api-stack \
    --capabilities CAPABILITY_IAM
