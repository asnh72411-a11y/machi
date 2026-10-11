import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    print("ERROR: MONGODB_URI is missing from .env")
    raise SystemExit(1)

client = MongoClient(
    uri,
    server_api=ServerApi("1"),
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
    print("SUCCESS: Connected to MongoDB Atlas!")

    db = client["simo_user"]
    users = db["users"]

    users.update_one(
        {"username": "simo_test"},
        {"$set": {"username": "simo_test", "role": "student"}},
        upsert=True
    )

    print("SUCCESS: Test user saved!")

except Exception as error:
    print("ERROR:", error)

finally:
    client.close()