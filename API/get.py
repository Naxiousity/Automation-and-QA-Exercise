
import requests

#Get all products list
r = requests.get('https://automationexercise.com/api/productsList')
print(r.json())

print(r.text)
