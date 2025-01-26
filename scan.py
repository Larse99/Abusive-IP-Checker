#!/usr/bin/python3

# Abuse IP scraper
# (C) Lars Eissink 2023

from includes.functions import *
from includes.parser import *
import sys

# Variables
# Changes these to your needs
api = ''


def main():
    if not len(sys.argv) > 1:
        print('no arguments have been given.')
        quit()

    # Set extended and json to False. Standard behaviour
    e = False
    j = False

    # Check if there is an valid IP
    if input_ip:
        if not check_ip(input_ip):
            print(f'Entered IP is invalid.')
            quit()

        ip = input_ip
        
    if input_extended:
        e = True
    
    if input_json:
        j = True

    # Everything checks out, lets see what it scored!
    check_score(api, ip, e, j)

if __name__ == '__main__':
    main()
