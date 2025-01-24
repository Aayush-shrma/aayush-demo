from pymongo import MongoClient

client = MongoClient("mongodb+srv://aayushsh8888:#9139#8816@aayush.hqzcf.mongodb.net/?retryWrites=true&w=majority&appName=aayush")
db = client["mero_database"]
collection = db["mero_collection"]
print("Conecction succresful ")

# document = {"name":"aayush","age":"19","location":"kathmandu"}
# collection.insert_one(document)

# document02 = {"name":"aay","age":"29","location":"mount"}
# collection.insert_one(document02)

# result = collection.delete_one({"name": "aay"})

# print("Deleted that document.")

new_values = {"$set": {"age": 30}} 

result = collection.update_one(filter, new_values)

print(f"Matched {result.matched_count} document(s), Modified {result.modified_count} document(s).")

