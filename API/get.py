
import requests
###This is sandbox only ehe

#Get all products list
#r = requests.get('https://automationexercise.com/api/productsList')

#print(r.json())


#Get user account detail by Email
params = {'email': 'notest@gmail.com'}
r = requests.get('https://automationexercise.com/api/getUserDetailByEmail', params=params)
print(r.json())

#Get all products list
# r = requests.get('https://automationexercise.com/api/brandsList')
# print(len(r.json()["brands"]))

# data = r.json()
# total = len(data["brands"])
# print(total)

# brands = data["brands"]
# unique = [item["brand"] for item in brands]
# uniques = set(unique)
# print(len(uniques))