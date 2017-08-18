"""
Usage:
primfeed view_feed
primfeed post <title> <body>
primfeed comment <postId> <title> <body>
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
        # self.apiURL = "http://34.207.10.230:3000/"
        super().__init__()

    @docopt_cmd()
    def view_feed(self, args):
        """Usage: view_feed"""
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(
            url, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            for post in response.json():
                print('Title: {}\nBody: {}\n'.format(
                    post['title'], post['body']))
                print()
        else:
            print("Please check your internet connection")
