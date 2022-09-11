import boto3

client=boto3.client("ec2")
client.delete_vpc(
    VpcId='vpc-07a4612947cd266de'
)