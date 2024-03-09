from Airquality.library import MongoClient

# Establish MongoDB connection and select database and collection
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
dar = db["dar-es-salaam"]