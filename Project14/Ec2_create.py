import boto3

ec2=boto3.resource("ec2")
ec2.create_instances(
    ImageId='ami-05fa00d4c63e32376',
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3,
    TagSpecifications=[
            {
                    'ResourceType': 'instance',
                    'Tags' : [{"Key": "Environment", "Value": "Prod"}]
                    
                                },
            ],
            
        )
    
instance= ec2.create_instances(
        ImageId="ami-05fa00d4c63e32376",
        InstanceType="t2.micro",
        MaxCount=3,
        MinCount=3,
        TagSpecifications=[
            {
                    'ResourceType': 'instance',
                    'Tags' : [{"Key": "Environment", "Value": "Prod"}]
                    
                                },
            ],
            
        )
print ("EC2 instances have been generated successfully")
