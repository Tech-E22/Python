import boto3

s3=boto3.client("s3")
objects=s3.list_objects(Bucket="esoflippinflybucket1")["Contents"] #list objects from the contents field

print(len(objects))

#View if there are any objects in bucket
if len(objects)>0:
    print("object exists")

#print out key values in bucket
for object in objects:
    print(object["Key"])