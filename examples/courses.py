from pyudemy import UdemyAffiliate

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"

udemy = UdemyAffiliate(client_id, client_secret)

print(udemy.courses())


test_filters = [
    {
        "Object": "course",
        "Setting": "@min",
        "Additions": ["description"],
        "Minus": ["title"],
    }
]

print(udemy.courses(fields=test_filters))
