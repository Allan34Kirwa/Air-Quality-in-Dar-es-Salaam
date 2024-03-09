from Airquality.library import PrettyPrinter
from Airquality.connection import dar

# Set up PrettyPrinter with indentation of 2 spaces.
pp = PrettyPrinter(indent=2)

#Use the find_one method to retrieve one document from the dar collection, 
# and assign it to the variable name result.
result = dar.find_one({})
pp.pprint(result)

# Retrieve distinct site values from metadata using 'dar' and assign to 'sites'
sites = dar.distinct('metadata.site')

# Aggregate and count readings per site using MongoDB's aggregation framework.
result = dar.aggregate(
    [
        {"$group": {"_id": "$metadata.site", "count": {"$count":{}}}}    
    ]
)
readings_per_site = list(result)
readings_per_site