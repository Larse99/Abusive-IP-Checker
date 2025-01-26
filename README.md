
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

# Check the reputation of an IP address
ipcheck [-i /  --ip] <ip>

# Get extended information about an IP address
ipcheck  -i  <ip> [-e /  --extended]

# Output the results as JSON
ipcheck [-i /  --ip] <ip>  [-j / --json]

# Show help
ipcheck [-h /  --help]
```

## License
This project is licensed under the **MIT License**. Feel free to use, modify, and share it as you wish!
