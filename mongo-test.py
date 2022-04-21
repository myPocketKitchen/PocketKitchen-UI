import datetime
import pymongo

client = pymongo.MongoClient("{}".format(srv))

food = client.food
records = food.records

Print("Food input")
food = input()

timestamp = datetime.datetime.now()

try: 
    records.insert_one(data)
except Exception as e: 
    print(e)
    pass