from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Ayush:ideal909@cluster0.sg4hsku.mongodb.net/?retryWrites=true&w=majority"
)

print(client.admin.command("ping"))