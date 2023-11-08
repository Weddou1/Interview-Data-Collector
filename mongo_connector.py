import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

def initiate_collection():
    load_dotenv()
    cluster = MongoClient(f"mongodb+srv://{os.getenv('USERNAME_CLUSTER')}:{os.getenv('PASSWORD_CLUSTER')}@cluster-test.fndbj.mongodb.net/UserData?retryWrites=true&w=majority")
    db = cluster["chirac"]
    collection = db["chirac"]
    return collection