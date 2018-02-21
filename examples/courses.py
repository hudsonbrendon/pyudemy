from pyudemy import Udemy
from decouple import config


client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')

udemy = Udemy(client_id, client_secret)

print(udemy.courses())
