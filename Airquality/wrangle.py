from Airquality.connection import dar
from Airquality.explore import pp
from Airquality.library import pd

# Create a wrangle function that will extract the PM2.5 readings from the site

# Test cell
result = dar.aggregate(
   [
       {"$match": {"metadata.site":11}},
     {"$group":{"_id": "$metadata.measurement", "count": {"$count": {}}}}
 ]
)
pp.pprint(list(result))

# From the output, we can see the 4 measurement types, temp, humidity, P1 and P2

# Query database for metadata with measurement "P2" and print first 3 results
result = dar.find({"metadata.measurement": "P2"}).limit(3)
pp.pprint(list(result))

# retrieve P2 values and timestamps, and print the first result
result = dar.find(
    {"metadata.site": 11, "metadata.measurement": "P2"},
    projection = {"P2":1, "timestamp":1, "_id":0}
)
pp.pprint(result.next())

# Create a DataFrame from query result, set timestamp as index, and display first few rows
df = pd.DataFrame(result).set_index("timestamp")
df.head()

# My wrangle function
def wrangle(collection):
    result = collection.find(
        {"metadata.site": 11, "metadata.measurement": "P2"},
        projection={"P2": 1, "timestamp": 1, "_id": 0},
    )

    df = pd.DataFrame(result).set_index("timestamp")
    
    # Localizing timestamps to timezone "Africa/Dar-es-Salaam"
    df.index = df.index.tz_localize("UTC").tz_convert("Africa/Dar_es_Salaam")
    
    # Remove all outlier PM2.5 readings for each hour
    df = df[df["P2"] <= 100]
    
    # Resample data & ffill missing values
    y = df["P2"].resample("1H").mean().fillna(method="ffill")
    
    # Return df
    return y