import unittest

import pytest

from infobip_channels.whatsapp.channel import WhatsAppChannel
from infobip_channels.whatsapp.models.path_parameters.manage_templates import (
    ManageTemplatesPathParameters,
)

from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv(".env")

INFOBIP_BASE_URL = os.getenv("INFOBIP_BASE_URL")
INFOBIP_API_KEY = os.getenv("INFOBIP_API_KEY")
RECIPIENT = os.getenv("RECIPIENT")

channel = WhatsAppChannel.from_auth_params({
    "base_url": INFOBIP_BASE_URL,
    "api_key": INFOBIP_API_KEY
})

response = channel.send_text_message(
    {
        "from": "447860099299",
        "to": "16477690077",
      "content": {
        "text": "Some text"
      },
      "callbackData": "Callback data",
      "notifyUrl": "https://www.example.com/whatsapp"
    }
)

print(response)

response = channel.send_image_message({
  "from": "447860099299",
  "to": "16477690077",
  "content": {
    "mediaUrl": "https://seekvectorlogo.com/wp-content/uploads/2019/06/infobip-vector-logo-small.png",
    "caption": "Check out our logo!"
  }
})

print(response)
