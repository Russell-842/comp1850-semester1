
import httpx

base_url = "https://dummyjson.com/"

content = "posts/1"
# Post 1 :
# 192 likes
# 25 dislikes
# 305 views
# User ID = 121

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)

# API call fragment for post 5, returning JSON data

# content = "posts/5"
# Post 5 :
# 119 likes
# 30 dislikes
# 626 views
# User ID = 131

# Constructing an API call to return all products mentioning "apple"
base_url2 = "https://dummyjson.com/products/search?q="

content2 = "apple"

url2 = base_url2 + content2 # API request

response = httpx.get(url2) # API call

print(response.status_code) # HTTP response

content2 = response.json() # JSON data

print(content2)

# Constructing an API call to return all "recipes" which are "snacks"
url3 = "https://dummyjson.com/recipes/meal-type/snack"

response = httpx.get(url3) # API call

print(response.status_code) # HTTP response

content3 = response.json() # JSON data

print(content3)
