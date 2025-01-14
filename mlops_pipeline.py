
import boto3
import time

# Function to deploy the model to AWS Lambda
def deploy_model_to_lambda(function_name, zip_file_path):
    lambda_client = boto3.client('lambda')
    
    with open(zip_file_path, 'rb') as f:
        zipped_code = f.read()
    
    response = lambda_client.update_function_code(
        FunctionName=function_name,
        ZipFile=zipped_code
    )
    print("Model deployed successfully:", response)

# Function to monitor the deployment
def monitor_model(function_name):
    logs_client = boto3.client('logs')
    log_group = f'/aws/lambda/{function_name}'
    
    response = logs_client.describe_log_streams(logGroupName=log_group)
    for stream in response['logStreams']:
        log_events = logs_client.get_log_events(
            logGroupName=log_group,
            logStreamName=stream['logStreamName']
        )
        for event in log_events['events']:
            print(event['message'])

# Example usage
if __name__ == '__main__':
    deploy_model_to_lambda('speech-recognition-function', 'speech_recognition.zip')
    time.sleep(10)
    monitor_model('speech-recognition-function')
