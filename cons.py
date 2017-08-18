import requests


def view_posts():
    url='https://jsonplaceholder.typicode.com/posts'
    response=requests.get(url, headers={"Content-Type":"application/json"})
    if response.status_code == 200:
        print ('Title |  Body')
        for post in response.json():
            print ('{} | {}'.format(post['title'], post['body']))
    else:
        print ("Check internet connection")


def add_posts():
    pass


def add_posts():
     url='https://jsonplaceholder.typicode.com/posts/'
    response=requests.get(url, headers={"Content-Type":"application/json"})
    if response.status_code == 200:
        print "Add Post"
        print ('Post |  Body')
        for comment in response.json():
            print ('{} | {}'.format(comment['name'], comment['body']))
    else:
        print ("Check internet connection")


def add_comment_on_post():
    pass


if __name__ == '__main__':
    view_posts()
