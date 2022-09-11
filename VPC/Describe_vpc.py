import boto3

client=boto3.client("ec2")
describe=client.describe_vpcs()
print(describe)
print(len(describe))

number_of_vpc=describe["Vpcs"]

for vpc in number_of_vpc:
    print(vpc["VpcId"])