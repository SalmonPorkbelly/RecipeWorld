import pymongo
import requests

client = pymongo.MongoClient("mongodb://localhost:27017")
DB_NAME = "recipe_world"
RECIPE_COLLECTION = "recipes"

url = "https://openapi.foodsafetykorea.go.kr/api/8237c9960a9f43b1abcc/COOKRCP01/json/1000/1114"
response = requests.get(url).json()
recipes = response['COOKRCP01']['row']

bulk_operation = []
for recipe in recipes:
    bulk_operation.append(
        pymongo.InsertOne({
            'name': recipe['RCP_NM'],
            'recipe': recipe
        })
    )

client[DB_NAME][RECIPE_COLLECTION].bulk_write(bulk_operation)