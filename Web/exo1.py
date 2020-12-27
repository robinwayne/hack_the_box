import requests 
from bs4 import BeautifulSoup 
import hashlib 


#site url to hit
url = "http://167.99.85.197:31142"
req=requests.session()

#get request
response = req.get(url)
if not response:
    print("code error: ", response.status_code)
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    tag = soup.h3
    code_to_md5 = tag.contents[0]
    print("code to encode: ", code_to_md5)
    result = hashlib.md5(code_to_md5.encode()).hexdigest()
    print("code encoded: ", result)
    myobj = {'hash':result}
    resp = req.post(url, data=myobj)
    print(resp.text)   

