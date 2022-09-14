import json
import boto3

# We are going to send a message with current time
from datetime import datetime

def lambda_handler(event, context):
 
    now = datetime.now()
    time_date = now.strftime("%H:%M:%S %m/%d/%Y")

    sqs = boto3.client('sqs')
   
# Url of the SQS queue you created and use your sns arn
    sqs.send_message(QueueUrl="https://sqs.us-east-1.amazonaws.com/XXXXXXXXX/your-queue-name",MessageBody=time_date)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processed')
    }