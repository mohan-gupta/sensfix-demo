from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mihirsinamdar:Tdkjibc9MyZOgkMz@cluster0.4frm5a0.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(uri,server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["Sensifix"]