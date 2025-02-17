#!/usr/bin/python3

# This file parses commands. ... And thats about it. I think it's beautiful
# Author: Lars Eissink 2023

import argparse

parser = argparse.ArgumentParser(description='Abuse Scraper: a tool designed to scrape Abuse IP statistics.')

# Arguments
parser.add_argument("positional_ip", nargs="?", help="IP address to scan (alternative to -i)")

# -i --address: Specify a address
parser.add_argument('-i', '--ip', help='Specify a IP address to scan')

# -e --extended: Show extended information about the IP address
parser.add_argument('-e', '--extended', action='store_true', help='Show extended information about the given IP address')

# -j --json: Show output in JSON.
parser.add_argument('-j', '--json', action='store_true', help='Shows output in JSON format.')

# -f --file: Load a file with IP-adresses
parser.add_argument('-f', '--file', help='Load a list of IP-addresses from file. Every IP needs to be on a single line.')

# Parse!
args = parser.parse_args()

# Error handling
if args.extended and args.json:
    parser.error('You cannot use extended and json output simultaneously.')

if args.ip and args.positional_ip:
    parser.error('You cannot define both: a positional argument and -i.')

# Assign values to variables
input_ip        =   args.ip or args.positional_ip
input_file      =   args.file
input_extended  =   args.extended
input_json      =   args.json