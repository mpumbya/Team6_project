import requests


def view_posts():
    """Method to view all posts on the feed"""
    url='https://jsonplaceholder.typicode.com/posts'
    response=requests.get(url, headers={"Content-Type":"application/json"})
    if response.status_code == 200:
        print ('Title |  Body')
        for post in response.json():
            print ('{} | {}'.format(post['title'], post['body']))
    else:
        print ("Check internet connection")


def add_posts():
    
    url='http://34.207.10.230:3000/posts'
    title = 'Team 6'
    body = 'Top post'
    response = requests.post(url, data = { 'title':title, 'body':body,'userId': 1 })
    post = response.json()
    
    if response.status_code == 200:
        print ('{} | {}'.format(post['title'], post['body']))
    else:
        print ("Check internet connection")
        
    pass


def view_comment_on_post(post_id):
    """Method to view comments on post with post_id"""
    url = 'https://jsonplaceholder.typicode.com/posts/'+str(post_id)+'/comments'
    response = requests.get(url, headers={"Content-Type":"application/json"})
    if response.status_code == 200:
        print "Comments on Post"
        print ('Comment by |  Body')
        for comment in response.json():
            print ('{} | {}'.format(comment['name'], comment['body']))
    else:
        print ("Check internet connection")


def add_comment_on_post():
    
    url = 'http://34.207.10.230:3000/comments'
    name = "Polo"
    email = "polo@points.sc"
    body = "We rock, as always"
    
    response = requests.post(
        url, data = { "postId":1, "name":name, "email":email,
        "body":body }
    )
    if response.status_code == 200:
        print ('{} | {}'.format(post['name'], post['body']))
    else:
        print ("Check internet connection")
        
    pass


if __name__ == '__main__':
    view_posts()
    view_comment_on_post(1)
    add_posts()
