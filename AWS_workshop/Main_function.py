
import boto3

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )

    print(response) # This will print the contents of the variable 'response' 

translate_text() # This line will call my function. 