from pymongo import MongoClient
from pymongo.server_api import ServerApi

from langchain import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_uri = os.getenv("MONGO_DB_URI")

client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db_name = os.getenv("DB")
db = client[db_name]

collection_cl1_name = os.getenv("COLLECTION_CAT_L1")
collection_cl2_name = os.getenv("COLLECTION_CAT_L2")
collection_val = os.getenv("COLLECTION_VALID")
collection_ticket = os.getenv("COLLECTION_TICKET")
collection_resp = os.getenv("COLLECTION_RESP")

openai_key1 = os.getenv("OPENAI_API_KEY_1")
openai_key2 = os.getenv("OPENAI_API_KEY_2")
openai_key3 = os.getenv("OPENAI_API_KEY_3")

llm1 = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_key1, temperature=1)
llm2 = OpenAI(model_name="gpt-3.5-turbo-0301", openai_api_key=openai_key2, temperature=1)
llm3 = OpenAI(model_name="gpt-3.5-turbo-0613", openai_api_key=openai_key3, temperature=1)