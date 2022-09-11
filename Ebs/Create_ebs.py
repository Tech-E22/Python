import boto3

ec2=boto3.client("ec2")

ec2.create_volume(AvailabilityZone='us-east-1a',
    Encrypted=False,
    Size= 12,
    SnapshotId='snap-08f1069dfde2007ba',
    VolumeType='gp2'
)