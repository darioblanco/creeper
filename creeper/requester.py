#!/usr/bin/env python
import argparse
import re

from ghost import Ghost


# Regex for checking if a url is correct
regex = re.compile(
    r'^(?:http)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Or ip
    r'(?::\d+)?'  # Optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


def parse_arguments():
    """Gets the console arguments"""
    parser = argparse.ArgumentParser(
        description='Creates random requests to a target url')
    parser.add_argument("url", type=valid_url, help=("Target url"))
    parser.add_argument("-a", "--auth", type=valid_auth, default=None,
                        help="Auth credentials in 'user:password' format")
    return vars(parser.parse_args())


def valid_url(url):
    """Checks that the given url has the proper format"""
    if not regex.match(url):
        raise argparse.ArgumentTypeError(
            "'{0}' is not a valid url".format(url))
    return url


def valid_auth(auth):
    """Checks that the given auth has the proper format"""
    try:
        user, password = auth.split(":")
    except:
        raise argparse.ArgumentTypeError(
            "'{0}' is not a valid auth".format(auth))
    return user, password


if __name__ == "__main__":
    arg_dict = parse_arguments()
    ghost = Ghost()
    print "Requesting '{0}'".format(arg_dict['url'])
    page, resources = ghost.open(arg_dict['url'], auth=arg_dict['auth'])
    print ghost.content