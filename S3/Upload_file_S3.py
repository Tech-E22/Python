import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="/Users/erika/Desktop/test.jpg",
    Bucket="Esoflippinflybucket1",
    Key="uploadtest.png"
)

#upload multiple files

import os
import glob

cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.jpg")

for file in files:
    s3=boto3.client('s3')
    s3.upload_file(
    Filename=file,
    Bucket="boto3-luit-jl7392384",
    Key=file.split("/")[-1]
    )