service_list = []

service_list.append("EC2")
service_list.append("Lambda")
service_list.append("DynamoDB")
service_list.append("S3")

print(service_list)
print(len(service_list))


# Remove by name
unwanted = ["S3", "EC2"]
 
for element in unwanted:
    service_list.remove(element)
    
print(service_list)
print(len(service_list))