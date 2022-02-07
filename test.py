import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "/transactions")
print(response.json())
input()

response = requests.get(BASE + "/transactions?page=2")
print(response.json())
input()

response = requests.get(BASE + "/transactions?page=5")
print(response.json())
input()


# response = requests.get(BASE + "/report")
# print(response.json())
