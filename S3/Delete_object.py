from urllib import response
import boto3

#Delete single object
s3=boto3.client("s3")
objects=s3.delete_object(Bucket="esoflippinflybucket1",Key="test.jpg")

#delete multiple objects
import os
import glob

objects=s3.list_objects(Bucket="esoflippinflybucket1")["Contents"]

for object in objects:
    s3.delete_object(Bucket="esoflippinflybucket1",Key=object["Key"])
    print(response)
    