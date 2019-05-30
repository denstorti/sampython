"""Return the pathname of the KOS root directory."""

import json

def return_message(ip_address):
    """Return information and IP"""

    print(type(ip_address))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip_address.text.replace("\n", "")
        })
    }
