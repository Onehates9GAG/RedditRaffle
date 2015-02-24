__author__ = 'Pannari'

import requests
import random

url = input("Please insert the URL: ")
url += '.json'

amount = input("Please insert the number of winners: ")
amount = int(amount)


r = requests.get(url, headers= { 'User-Agent': 'RedditRaffle - Randomize user from thread! (by /u/FallenSupport)' })

data = r.json()

a = []

for doc in data[1]["data"]["children"]:
    a.append(doc["data"]["author"])

random.shuffle(a)
winners = a[:amount]

print(winners)
#print (data)
