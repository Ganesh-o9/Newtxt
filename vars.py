#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22182189"))
API_HASH = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = environ.get("BOT_TOKEN", "8165163889:AAH-vcFtoaBj-OSLbnKOf1D41xVqvispczA")

OWNER = int(environ.get("OWNER", "6256788018"))
CREDIT = environ.get("CREDIT", "𝗞𝗮𝗿𝗮𝗻'𝘀 𝗕𝗼𝘁")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5215296789,-1002751894880').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5215296789,-1002751894880').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
