import requests

def view_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url, headers={"Content-Type":"application/json"})
    if response.status_code == 200:
        print ('Title |  Body')
        for post in response.json():
            print ('{} | {}'.format(post['title'], post['body']))
    else:
        print("Check internet connection")

def add_post(title, body):
    url = 'http://34.207.10.230:3000/posts'
    response = requests.post(url, data = { 'title':title, 'body':body,'userId': 2 })
    if response.status_code == 200:
        post = response.json()
        print ('{} | {}'.format(post['title'], post['body']))
    else:
        print("Could not post, check internet connection")
    pass

def view_comment_on_post():
    pass

def add_comment_on_post():
    pass

if __name__ == '__main__':
    add_post('Team 6', 'Top posts')
