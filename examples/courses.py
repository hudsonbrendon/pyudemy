from decouple import config
from pyudemy import Udemy

client_id = config("CLIENT_ID")
client_secret = config("CLIENT_SECRET")

udemy = Udemy(client_id, client_secret)

print(udemy.courses())
