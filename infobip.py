from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from infobip_channels.sms.channel import SMSChannel

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

def send_sms(message):
    with app.app_context():
        try:
            infobip_client = SMSChannel.from_auth_params(
                {
                    "base_url": INFOBIP_BASE_URL,
                    "api_key": INFOBIP_API_KEY
                }
            )
            
            phone_number = RECIPIENT

            response = infobip_client.send_sms_message(
                {
                    "messages": [
                        {
                            "destinations": [{"to": phone_number}],
                            "text": message,
                        }
                    ]
                }
            )

            return jsonify({"success": True, "response": response.messages})
        except Exception as e:
            return jsonify({"success": False, "error": str(e)})

# If this script is run directly, run the send_sms function
if __name__ == "__main__":
    send_sms("Hey it's William")
