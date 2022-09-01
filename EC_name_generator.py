import string
import random

def generate_random_name(instance_length,instance_combinations):
    generated_string = ""  
    for _ in range(instance_length): 
        random_character = random.choice(instance_combinations)
        generated_string += random_character 
    return generated_string 

number_of_ec2_instanes = int(input("Please enter the number of EC2 instances you would like to create: "))
ec2_department = input("Please enter the department name: ") 


instance_length = 10 
instance_combinations = string.ascii_uppercase + string.ascii_lowercase + string.digits 


ec2_names = [] 
ec2_instances = [] 

for _ in range(0,number_of_ec2_instanes): 
    generated_name = generate_random_name(instance_length,instance_combinations)  
    while generated_name in ec2_names: 
        generated_name = generate_random_name(instance_length,instance_combinations)  
    ec2_names.append(generated_name) 


for name in ec2_names: 
    ec2_instances.append(ec2_department + '_' + name)
    
print(ec2_instances)