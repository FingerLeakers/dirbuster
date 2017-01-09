from __future__ import print_function
from os import system
from sys import platform
import argparse
import requests


def clear_screen():
    if platform.startswith('linux'):
        system('clear')
    else:
        system('cls')


def print_banner():
    print("""

  _____           _ _
 |  __ \         | (_)
 | |__) |   _  __| |_ _ __
 |  ___/ | | |/ _` | | '__|
 | |   | |_| | (_| | | |
 |_|    \__, |\__,_|_|_|
         __/ |
        |___/

[+]Github:   github.com/nash0x27
[+]Email:    gabrieldutra-08@protonmail.com
[+]Facebook: fb.com/n4shxx

=============================================

""")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='target to explore (e.g.: google.com)')
    args = parser.parse_args()

    with open('wordlist/wordlist.txt') as wordlist1:
        endpoints = wordlist1.readlines()
        url_base = args.target if args.target.startswith('http') else 'http://' + args.target
        for endpoint in endpoints:
            error = 404
            url = '{}/{}'.format(url_base, endpoint).strip()
            if endpoint[0] != "#":
                response = requests.get(url)
                error = response.status_code
            print('[{1}] {0}'.format(url, error))

if __name__ == '__main__':
    clear_screen()
    print_banner()
    main()
