import boto3

ec2=boto3.resource("ec2")
createinstance= ec2.create_instances(
    ImageId='ami-05fa00d4c63e32376',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'dev-environment',
                },
                {                    
                    'Key': 'environment',
                    'Value': 'dev',
                },
            ]
        },
    ],
)
#Print out each instance that is created
for instanceid in createinstance:
    print("Here are your instance id for dev environment:", instanceid)