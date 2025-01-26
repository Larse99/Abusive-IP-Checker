#!/usr/bin/python3

#Parser files
# This file parses commands. ... And thats about it. I think it's beautiful
# Author: Lars Eissink 2023

import argparse

parser = argparse.ArgumentParser(description='Abuse Scraper: a tool designed to scrape Abuse IP statistics.')

# Arguments
# -i --address: Specify a address
parser.add_argument('-i', '--ip', help='Specify a IP address to scan')

# -e --extended: Show extended information about the IP address
parser.add_argument('-e', '--extended', action='store_true', help='Show extended information about the given IP address')

# -j --json: Show output in JSON.
parser.add_argument('-j', '--json', action='store_true', help='Shows output in JSON format.')

# Parse!
args = parser.parse_args()

# Error handling
if (args.extended and args.json):
    parser.error('You cannot use extended and json output simultaneously.')

if (args.extended and not args.ip):
    parser.error('Please enter a valid IP. This cannot be empty.')

if (args.json and not args.ip):
    parser.error('Please enter a valid IP. This cannot be empty.')

# Assign values to variables
input_ip        =   args.ip
input_extended  =   args.extended
input_json      =   args.json

