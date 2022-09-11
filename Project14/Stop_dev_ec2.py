import boto3

ec2 = boto3.client('ec2')

# Environment tag with value dev, so it can find the proper instance
tags={'Name': 'tag:environment','Values': ['dev']}

# Looks for instances specified that are running
running={'Name': 'instance-state-name', 'Values': ['running']}

for each_instance in ec2.describe_instances(Filters=[tags,running])['Reservations']:
    for inst_id in each_instance['Instances']: 
        ec2.stop_instances(InstanceIds=[inst_id['InstanceId']]) 
        print("The following instances are stopping: ", [inst_id['InstanceId']])