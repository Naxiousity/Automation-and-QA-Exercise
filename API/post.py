import requests

#POST to All Products List

r = requests.post('https://automationexercise.com/api/productsList')
response = r.json()

print(r.status_code)
print(response)