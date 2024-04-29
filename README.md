# AWS-base-image-docker-Lambda

This is a simple python script to return the aws account_id.
To test locally, you will need to fill in the access_key and secret_key.

# Dockerfile for AWS Lambda Python Function

This Dockerfile is used to build a Docker image for an AWS Lambda function written in Python.

### Usage

To use this Lambda function, follow these steps:
1. Create a new private repository in Amazon ECR:
- Ex: account_id.dkr.ecr.us-east-1.amazonaws.com/lambda
2. Retrieve an authentication token and authenticate your Docker client to your registry
- aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin account_id.dkr.ecr.us-east-1.amazonaws.com
3. Build your Docker image
- docker build -t lambda .
4. Tag your image so you can push
- docker tag lambda:latest account_id.dkr.ecr.us-east-1.amazonaws.com/lambda:latest
5. Push this image to your newly created AWS repository
- docker push account_id.dkr.ecr.us-east-1.amazonaws.com/lambda:latest
7. Create a Lambda function in AWS Lambda.
8. Configure the Lambda function to use the container image from the container registry.
9. click on test

### Test Local
1. docker build -t lambda_scraping .
2. docker run -e LOCAL_EXECUTION=true -p 9000:8080 lambda_scraping:latest
3. curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"test":"test"}'
