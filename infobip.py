from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from infobip_channels.mms.channel import MMSChannel

load_dotenv(".env")

INFOBIP_BASE_URL = os.getenv("INFOBIP_BASE_URL")
INFOBIP_API_KEY = os.getenv("INFOBIP_API_KEY")
RECIPIENT = os.getenv("RECIPIENT")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def backend_function():
    response = jsonify({"msg": "Backend function called successfully", "text": "test"})
    response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:5173")
    return response

def send_sms(recipient, message):
    with app.app_context():
        try:
            infobip_client = MMSChannel.from_auth_params(
                {
                    "base_url": INFOBIP_BASE_URL,
                    "api_key": INFOBIP_API_KEY
                }
            )
            
            phone_number = recipient

            response = infobip_client.send_mms_message(
                {
                    "messages": [
                        {
                            "destinations": [
                                {
                                    "to": "14168807375"
                                }
                            ],
                            "from": "InfoMMS",
                            "messageSegments": [
                                {
                                    "text": "This is a sample message"
                                },
                                {
                                    "contentId": "320px-Depth_of_field_Cat.jpg",
                                    "contentType": "image/jpeg",
                                    "contentUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Depth_of_field_Cat.jpg/320px-Depth_of_field_Cat.jpg"
                                }
                            ],
                            "title": "This is sample subject"
                        }
                    ]
                }
            )

            return jsonify({"success": True, "response": response.messages})
        except Exception as e:
            return jsonify({"success": False, "error": str(e)})

# If this script is run directly, run the send_sms function
if __name__ == "__main__":
    send_sms("14168807375", "Hey it's William")
