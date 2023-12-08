from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from pymongo.server_api import ServerApi
import time
from dotenv import load_dotenv
import os

load_dotenv()

uri=os.getenv('uri')

#handling db connection error
max_retries=3 # defining max no to retries to be performed

def connect_to_database():
    for i in range(max_retries):
        try:
            # Create a new client and connect to the server
            client = MongoClient(uri, server_api=ServerApi('1'))
            client.admin.command('ismaster')
            return client
        # at connection failure
        except (ConnectionFailure, ServerSelectionTimeoutError) as e:
            print(f"Attempt {i+1} of {max_retries}: Cannot connect to the server. Retrying in 3 seconds")
            print(f"error code: {e}")
            time.sleep(3) #time after which again to retry
    raise ConnectionError("failed to connect to the database after multiple attempts")

try:
    db_client=connect_to_database()
except ConnectionError as e:
    print(e)

db=db_client["books"]
collection=db["test"]