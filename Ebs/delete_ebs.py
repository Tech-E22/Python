import boto3

ec2=boto3.client("ec2")

ec2.delete_snapshot(SnapshotId='snap-08f1069dfde2007ba')