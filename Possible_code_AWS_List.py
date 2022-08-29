"""
    Program:
    Create a list of services using Python. IE: S3, Lambda, EC2, etc
    2. The list should be empty initially.
    3. Populate the list using append or insert.
    4. Print the list and the length of the list.
    5. Remove two specific services from the list by name or by index.
    6. Print the new list and the new length of the list.

"""

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