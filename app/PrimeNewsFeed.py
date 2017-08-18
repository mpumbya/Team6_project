"""
Usage:
primfeed view_feed
primfeed post <title> <body>
primfeed add_comment <postId> <title> <body>
primfeed view_comments <post_id>
options:
quit    to exit the application
"""

import cmd
import requests
import json
import os
from docopt import DocoptExit, docopt
from pyfiglet import Figlet, DEFAULT_FONT
from colorama import Fore, init, Back, Style


def intro():
    print(__doc__)


def docopt_cmd(func):
    """
    This decorator simplifies the try/except block and returns
    the result of parsing docopt using an action

    credits: https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
    Contributors: JonLundy, TheWaWaR
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as err:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(err)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class PrimeNewsFeed(cmd.Cmd):
    os.system("cls")
    prompt = "primfeed>>> "
    font = Figlet(DEFAULT_FONT)
    print("{}{}{}".format(Fore.YELLOW,
                          font.renderText("A Primitive News Feed"), __doc__))

    def __init__(self):
        self.apiURL = "https://jsonplaceholder.typicode.com/posts"
        super().__init__()

    @docopt_cmd
    def do_view_feed(self, args):
        """Usage: view_feed"""

        response = requests.get(
            self.apiURL, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            for post in response.json():
                print('Title: {}\nBody: {}\n'.format(
                    post['title'], post['body']))
                print()
        else:
            print("Please check your internet connection")

    @docopt_cmd
    def do_post(self, args):
        """Usage: post <title> <body>"""
        body = args['<body>']
        title = args['<title>']

        data = dict(title=title, body=body)
        headers = {"Content-Type": "application/json", "Accept": "text/plain"}
        post_url = "http://34.207.10.230:3000/posts"
        resp = requests.post(post_url, data=json.dumps(data), headers=headers)
        if int(resp.status_code) == 201:
            print("Your data has been posted")
        else:
            print("You have an error somewhere in your code")
        print()

    @docopt_cmd
    def do_add_comment(self, args):
        """Usage: add_comment <postId> <title> <body>"""
        postId = args["<postId>"]
        title = args["<title>"]
        body = args["<body>"]

        data = dict(postId=postId, title=title, body=body)
        headers = {"Content-Type": "application/json", "Accept": "text/plain"}

        comment_url = "http://34.207.10.230:3000/comments"
        r = requests.post(comment_url, data=json.dumps(data), headers=headers)
        if int(r.status_code) == 201:
            print("Your comment has been registered /posted")
        else:
            print("We are having trouble posting your comment")
        print()

    @docopt_cmd
    def do_view_comments(self, args):
        """usage: view_comments <post_id>"""

        post_id = args["<post_id>"]
        url = 'https://jsonplaceholder.typicode.com/posts/' + \
            str(post_id) + '/comments'
        response = requests.get(
            url, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            for comment in response.json():
                print('Name: {}\nBody: {}\n'.format(
                    comment["name"], comment['body']))
        else:
            print("You might be having trouble with your internet connection")

    def do_quit(self, args):
        """Usage: quit"""
        os.system('cls')
        print('Application Exiting')
        exit()

PrimeNewsFeed().cmdloop()
