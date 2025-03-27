# app.py
import json

def main(event, context):
    body = {
        "message": "Hello from app.py! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

