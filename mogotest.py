import pymongo
from pymongo import MongoClient

# connection to the database
cluster = MongoClient("mongodb+srv://studymode:Popping112@cluster0-pc3kg.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["studymode"]
collection = db["links"]

post = {"_id": "4TK4", "name": "4tk4", "link": "mcmaster.ca"}
# collection.insert_one(post)
# can also insert many by inset_many([post1,post2])

results = collection.find(post)
# can also search with regular expression
print(results)

for result in results:
    print(result)
    print(result["link"])

post_count = collection.count_documents({})
print(post_count)