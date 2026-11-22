
# Task 1 - Using httpx

We will use a simple source of web data: [HTTPbin](https://httpbin.io/json)

This provides synthetic data and a REST API, with no authentication, for testing code.

## Create a virtual environment

See slide on `Installing httpx CLI`

## Install httpx

`pip install 'httpx[cli]'`

## Command-line use

We can fetch data for a single post from the API with

`httpx https://httpbin.io/json​`

Note the reply and identify:
- HTTP status code
- HTTP header
- Data (this format is called JSON, we will discuss it next)

# Reply : 
# HTTP status code = HTTP/1.1 200 OK
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Thu, 19 Nov 2026 16:23:38 GMT
Content-Length: 421

{
    "slideshow": {
        "author": "Yours Truly",
        "date": "date of publication",
        "slides": [
            {
                "title": "Wake up to WonderWidgets!",
                "type": "all"
            },
            {
                "items": [
                    "Why <em>WonderWidgets</em> are great",
                    "Who <em>buys</em> WonderWidgets"
                ],
                "title": "Overview",
                "type": "all"
            }
        ],
        "title": "Sample Slide Show"
    }
}

## Other response codes

What is the difference if we request content that does not exist?

`httpx https://httpbin.io/jsoon​`

# Reply :
# Error comes up, stating 'Not Found'
HTTP/1.1 404 Not Found
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Content-Type: application/json; charset=utf-8
Date: Thu, 19 Nov 2026 16:25:23 GMT
Content-Length: 49

{
    "status_code": 404,
    "error": "Not Found"
}
