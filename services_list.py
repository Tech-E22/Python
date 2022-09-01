service_list = []
print("Initial empty list: " , service_list)


service_list.append("EC2") # append EC2 to end of list
print("List after one append: " , service_list)


service_list.insert(0, "Lambda") # insert Lambda at index 0 (front of list)
print("List after insert at position 0: " , service_list)


service_list.insert(1, "DynamoDB") # insert DynamoDB at index 1 (middle of list)
print("List after insert at position 1: " , service_list)


service_list.insert(len(service_list), "Cloud9") # insert Cloud9 at the end of list (same as append)
print("List after insert at last position: " , service_list)




print("Printing the whole list: " , service_list)
print("The length of the list is: " , len(service_list)) # len() is used to prin the length of the list

print("Print specific index of list (2): ", service_list[2])


service_list.remove("EC2") # remove first occurance of EC2 from list
print("List after removing first occurance of word EC2: " , service_list)


service_list.pop(1) # pop element at index 1 in this case DynamoDB (if left blank it defaults to end of list)
print("List after removing element at index number 1: " , service_list)


print("------------------------------------------------------------------------ Remove items by index")
service_list.extend(["EC2","DynamoDB"]) # append all elements at the end of the list
print("New List: " , service_list)


# Remove by index
# given index of elements  removes 0 2 and 3 indexes
unwanted = [0, 2]
 
for element in sorted(unwanted, reverse = True):
    service_list.pop(element)
    
print("List after removing element at indexes 0,2,3 : " ,service_list)

"""
Though indexes of elements in known, deleting the elements randomly will change the values of indexes. 
Hence, it is always recommended to delete the largest indices first. 
Using this strategy, index of smaller values will not be changed. 
We can sort the list in reverse order and delete the elements of list in descending order.
"""


    
print("------------------------------------------------------------------------ Remove items by name")
service_list.extend(["EC2","DynamoDB", "Lambda"]) # append all elements at the end of the list
print("New List: " , service_list)

 
# Remove by name
unwanted = ["Cloud9", "EC2"]
 
for element in unwanted:
    service_list.remove(element)
    
print("List after removing elements EC2 and Cloud9 : " ,service_list)




print("Printing the whole list: " , service_list)
print("The length of the list is: " , len(service_list)) # len() is used to prin the length of the list