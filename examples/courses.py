from pyudemy import Udemy
from decouple import config


client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')

udemy = Udemy(client_id, client_secret)

print(udemy.courses())


test_filters = [{ #Can be used to control return data from API
 "Object": "course",
 "Setting": "@min",
 "Additions": ["description"],   
 "Minus": ["title"]
 }]

print(subcategory = "Cryptocurrency & Blockchain", udemy.courses(fields = test_filters)) #Bug would previously occur for categories with & in title
