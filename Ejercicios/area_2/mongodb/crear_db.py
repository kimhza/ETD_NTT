import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

if myclient:
    print("Conectado")

# mydb = myclient["mydatabase"]
