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
        print('You must provide an IP address (-i <ip>) or a file (-f <file>).')
        sys.exit(1)

    # Set extended and json to False. Standard behaviour
    e = False
    j = False

    # Check if JSON and Extended are set
    if input_extended:
        e = True
    
    if input_json:
        j = True

    # Check individual IP
    if input_ip:
        if not check_ip(input_ip):
            print(f'Entered IP is invalid.\n')
            sys.exit(1)

        ip = input_ip
        check_score(api, ip, e, j)

    # Check if a file path is given
    if input_file:
        read_from_file(api, input_file, e, j)
    
if __name__ == '__main__':
    main()