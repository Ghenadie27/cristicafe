import json
import boto3
import uuid
import time
from botocore.exceptions import ClientError
from datetime import datetime
from json import dumps

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = "form"  # Replace with your table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):

    # def serialize_sets(obj):
    #     if isinstance(obj, set):
    #         return list(obj)
    #     return obj

    try:        
        # Parse the request body
        body = json.loads(event.get('body', '{}'))
        print(body)
        #body = json.dumps(body)
        #print(body)
        print(type(body))
        name = body.get('name')
        #print(name)
        email = body.get('email')
        # phone = body.get('phone')
        # #print(phone)
        # time = body.get('time')
        # #print(time)
        # date = body.get('date')
        # #print(date)
        # number = body.get('number')
        # #print(number)
        message = body.get('message')
       #print(message)

        # Validate inputs
        if not name: #or not phone or not time or not date or not number:
            return {
                "statusCode": 400,
                'headers': {"Access-Control-Allow-Origin": "*",
                },
                "body": json.dumps({"error": "Missing required fields"}),
                "isBase64Encoded": False
            }
            
        # Create a unique identifier and timestamp
        item_id = str(uuid.uuid4())
        #timestamp = str(int(time.time()))
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

        # Save data to DynamoDB
        table.put_item(
            Item={
                'id': item_id,       # Unique identifier
                'name': name,
                'email': email,
                # 'phone': phone,
                # 'time': time,
                # 'date': date,
                # 'people': number,                
                'message': message,
                'timestamp': timestamp  # Unix timestamp
            }
        )

        return {
            "statusCode": 200,
            'headers': {"Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"Data submitted successfully"}),
            "isBase64Encoded": False
        }

    # except TypeError:
    #     pass
       
    except ClientError as e:
        return {
            "statusCode": 500,
            'headers': {"Access-Control-Allow-Origin": "*",
                },
            "body": json.dumps({"error": "DynamoDB Error", "details": str(e)}),
            "isBase64Encoded": False
        }
                
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            'headers': {"Access-Control-Allow-Origin": "*",
                },
            "body": json.dumps({"error": "Invalid JSON input"}),
            "isBase64Encoded": False
        }
      
    except Exception as e:
        return {
            "statusCode": 500,
            'headers': {"Access-Control-Allow-Origin": "*",
                },
            "body": json.dumps({"error": str(e)}),
           "isBase64Encoded": False
            }      

    