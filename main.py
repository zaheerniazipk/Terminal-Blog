import pymongo

URI = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(URI)

database = client['fullstack']
collection = database['students']

# List comprehension
students = [student for student in collection.find({})]
print(students)