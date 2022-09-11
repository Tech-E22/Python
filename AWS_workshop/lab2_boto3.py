import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
# Place text below    
    print(response) # this will print the contents of the variable  

translate_text() # This will call my function


    