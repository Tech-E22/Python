#testing to see if code will commit

#Python Project Week 12. List of AWS Services.

#Create an empty list

aws_services = []

#Append or Input Items to your List

aws_services.insert(0, "Lambda")
aws_services.append("EC2")
aws_services.append("ECS")
aws_services.append("S3")
aws_services.append("CodeBuild")

#aws_services += ['Lambda', 'EC2', 'ECS', 'S3', 'CodeBuild']

print("List of AWS Services")
print(*aws_services)
print("The number of services in this list is:", len(aws_services))
print("Let's make list even shorter.")
print("I want to get rid of Lambda and EC2.")

#Delete first two services
del aws_services[0]
del aws_services[0]

print(*aws_services)
print("The number of services in this list now:", len(aws_services))

print("I think we completed the steps")

#Researched some more and decided to edit the list and change the coding and naming convention

aws_service_list = []

aws_service_list.append("lambda")
aws_service_list.append("EC2")
aws_service_list.append("ECS")
aws_service_list.append("S3")
aws_service_list.append("CodeBuild")

print(aws_service_list)
print(len(aws_service_list))


#Delete services by name
unwanted = ["S3", "EC2"]
 
for element in unwanted:
    aws_service_list.remove(element)
    
print(aws_service_list)
print(len(aws_service_list))

