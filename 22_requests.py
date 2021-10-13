import requests
import json

r = requests.get('https://images.unsplash.com/photo-1634039958874-cf2255b361bd?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDF8UzRNS0xBc0JCNzR8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60')

with open('fashion.png', 'wb') as f:
    f.write(r.content)    # r.content returns the binary of the content

# print(r.text)              r.text returns the html text
print(r.status_code)     # r.status_code returns the status code of the http request.
print(r.ok)             # r.ok returns for status code< 400 else false
print(r.headers)        # returns the header of the request

payload = {
    'page':2,
    'count':25
}
user ={
    "username" : "arko",
    "password" : "zuyj"
}
r2 = requests.get('https://www.w3schools.com/tags/tag_bdo.asp',params=payload)
#print(r2.url)

r3 = requests.post('https://www.w3schools.com/tags/tag_bdo.asp',data=user)
print(r3.url)
