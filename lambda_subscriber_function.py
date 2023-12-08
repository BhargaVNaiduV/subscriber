import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(" we are printing the message that we got from sqs queue")
    print("The present employe detais that are processed from a queue is ")
    print(event["Records"][0]["body"])
    event_body_dict = json.loads(event["Records"][0]["body"])
    print("The GUID of the message is ", event_body_dict["message_guid"] )
    
    table_name = 'EmployeeDetails'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    payload = event_body_dict
    response = table.put_item(Item=payload)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Data written to DynamoDB!')
    }
    
