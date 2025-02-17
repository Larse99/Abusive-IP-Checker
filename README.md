
# Abusive IP Checker

The **Abusive IP Checker** is a simple CLI utility that lets you check the reputation of IP addresses using AbuseIPDB. No need to open a browser—just run the tool directly from your terminal!

## Prerequisites

Before using this utility, you'll need an API key from AbuseIPDB. You can obtain one by signing in at [AbuseIPDB](https://www.abuseipdb.com). The default free plan provides up to 1,000 requests per day. If you need more, signing up as a "Webmaster" gives you approximately 10,000 requests per day.

## Installation

To install the tool, simply run the `INSTALL.sh` script as root or with `sudo`. Elevated privileges are needed to place the files in the appropriate system directories. By default, the files are installed in `/opt`, but you can modify the `INSTALL.sh` script to suit your needs.

### Adding Your API Key

For now, you need to manually add your AbuseIPDB API key to the `scan.py` file in the installation directory (default: `/opt/Abusive-IP-Checker/scan.py`). Update the `api` variable at the top of the file.

In a future update, the API key setup will be included as part of the installation process, and a configuration file stored in your home directory will be used instead.

**Note:** Since this script can be used by all system users, any API key added will serve as the default for everyone.

## Usage

This utility is straightforward to use. Run `ipcheck -h` to see all available options. Below is a quick summary:

```bash
# Arguments in '[]' indicate either option can be used (e.g., --ip or -i).
# Either -i or -f can be combined with --extended or --json.

# Check the reputation of an IP address
ipcheck [-i /  --ip] <ip>

# Get extended information about an IP address
ipcheck  -i  <ip> [-e /  --extended]

# Output the results as JSON
ipcheck [-i /  --ip] <ip>  [-j / --json]

# Use a file as input
ipcheck [-f / --file] <file>

# Show help
ipcheck [-h /  --help]
```

### Example file usage
```txt
66.249.76.162
66.249.76.161
66.249.76.160
66.249.76.164
66.249.76.165
66.249.76.163
66.249.76.166
66.249.76.167
66.249.76.168
66.249.76.169
66.249.76.170
```

## License
This project is licensed under the **MIT License**. Feel free to use, modify, and share it as you wish!
