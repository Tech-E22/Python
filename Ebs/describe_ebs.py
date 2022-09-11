import boto3

ec2=boto3.client("ec2")

ec2.describe_snapshots(SnapshotIds=['snap-08f1069dfde2007ba'])