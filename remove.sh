#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="zaha-crm-api-deployment-workspace-12345"

# Delete CloudFormation Stack
aws cloudformation delete-stack \
    --stack-name zaha-crm-api-stack

# Delete non-empty bucket
aws s3 rb s3://$BUCKET --force
