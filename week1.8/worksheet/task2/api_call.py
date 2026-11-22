
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
base_url = "https://dummyjson.com/products/search/apple"


