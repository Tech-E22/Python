import boto3 
# Service resource
sqs = boto3.resource('sqs')

# Create the queue
queue = sqs.create_queue(QueueName='week15queue')

# Identifiers and attributes
print(queue.url)