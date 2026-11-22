"""
Task 2: Fetch and display a post Using GET Request
"""
# Import module - pip install httpx
import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

# Test in terminal 
# import httpx
# response.status_code # prints '200' if successful
# response.is_success # prints 'True' if successful

if response.is_success:
    print(response.json())      # response object, json() method

# Response code :
{'slideshow': {'author': 'Yours Truly', 'date': 'date of publication', 'slides': 
[{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, 
{'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 
'title': 'Overview', 'type': 'all'}], 'title': 'Sample Slide Show'}}
