import requests
url = 'http://34.207.10.230:3000/posts'
data = '{ "id" }'
response = requests.get(url, data=data,headers={"Content-Type": "application/json"})
print(response)
#sid=response.json()['platform']['login']['sessionId']   
print(response.text)
#print(sid)