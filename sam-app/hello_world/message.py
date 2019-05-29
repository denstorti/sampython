import json
import requests

def returnMessage(ip):
    print(type(ip))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        })
    }
