import boto3
import os

access_key='xxx'
secret_key='xxx'


def handler(event, context):
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:", context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
    
    if 'LOCAL_EXECUTION' in os.environ:
        sts = boto3.client('sts',aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    else:
        sts = boto3.client('sts')
    return sts.get_caller_identity()["Account"]
