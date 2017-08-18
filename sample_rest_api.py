import requests

# GET 1 POST
url = 'http://34.207.10.230:3000/posts/1'

# GET POSTS
url = 'http://34.207.10.230:3000/posts'

# GET COMMENTS FOR POST 1
url = 'http://34.207.10.230:3000/posts/1/comments'

# GET POSTS
response = requests.get(
    url,
    headers = {"Content-Type": "application/json"}
)

# POST
''' response = requests.post(
    url, 
    data = { 'title':'foo', 'body':'bar','userId': 1 }
) '''

# POST COMMENT
''' response = requests.post(
    url, 
    data = { "postId":1, "id":1, "name":"Elise", "email":"Eliseo@gardner.biz", 
    "body":"laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo n" }
) '''

print(response)
print(response.text)
#sid = response.json()['platform']['login']['sessionId']   // to extract the detail from response
#print(sid)