#!/usr/bin/python3

# Main functions file
# Author: Lars Eissink 2023

import re
import requests
import sys

def check_ip(ip_address):
    # IPv4 pattern and regular expression match
    ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    ipv4_match = re.match(ipv4_pattern, ip_address)
    
    # Check if entered IPv4 address is valid
    if ipv4_match:
        octets = ip_address.split(".")
        if (
            all(0 <= int(octet) <= 255 for octet in octets)
            and octets[0] != "0"
            and octets[-1] != "0"
            and ip_address != "0.0.0.0"
            and ip_address != "127.0.0.1"
        ):
            return True
        
    # IPv6 pattern and regular experssion match
    ipv6_pattern = r"^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$"
    ipv6_match = re.match(ipv6_pattern, ip_address)

    # Check if entered IPv6 address is valid
    if ipv6_match:
        segments = ip_address.split(":")
        if all(0 <= int(segment, 16) <= 65535 for segment in segments):
            return True
    
    return False

# Checks the information about a given IP
def check_score(api=None, ip_address=None, extended=False, json=False):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}'
    headers = {
        'Key': api,
        'Accept': 'application/json'
    }

    # Set up API Connection
    response = requests.get(url, headers=headers)

    # If the response is not 200, exit
    if response.status_code != 200:
        print('Connection to AbuseIPDB failed. Please check your API key!')
        sys.exit(1)

    # Check if user requested extended information
    if extended == True:
        data = response.json()
        print(f'IP Address: {data["data"]["ipAddress"]}')
        print(f'Hostnames: {data["data"]["hostnames"]}')
        print(f'Domain: {data["data"]["domain"]}')
        print(f'ISP: {data["data"]["isp"]}')
        print(f'Country: {data["data"]["countryCode"]}')
        print(f'Abuse Score: {data["data"]["abuseConfidenceScore"]} Reported: {data["data"]["totalReports"]} times.\n')
    
    if extended == False and json == False:
        data = response.json()
        print(f'IP Address: {data["data"]["ipAddress"]}')
        print(f'Abuse Score: {data["data"]["abuseConfidenceScore"]}')
        print(f'Country: {data["data"]["countryCode"]}\n')
    
    if json == True:
        data = response.json()
        print(data)

# Read IP addresses from file and checks the score of each
def read_from_file(api, file_path, extended=False, json=False):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                ip = line.strip()

                if not check_ip(ip):
                    print(f'Entered IP is invalid: {ip}\n')
                    sys.exit(1)

                check_score(api, ip, extended, json)
    except FileNotFoundError:
        print(f'Error: File not found: {file_path}', file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f'Error: Incorrect permissions: {file_path}', file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f'Error while opening the file: {file_path}: {e}', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}', file=sys.stderr)
        sys.exit(1)