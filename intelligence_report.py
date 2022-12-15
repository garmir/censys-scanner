import argparse
import json
import requests
import socket

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--uid", required=True, help="Censys API UID")
parser.add_argument("--secret", required=True, help="Censys API secret")
parser.add_argument("--domain", required=True, help="target domain name")
args = parser.parse_args()

# Query Censys API to get IP addresses and subdomains related to the target domain
url = f"https://search.censys.io/api/v2/hosts/search?q=name%3A%20{args.domain}&per_page=50&virtual_hosts=INCLUDE"
headers = {"Content-Type": "application/json"}
auth = (args.uid, args.secret)

response = requests.get(url, headers=headers, auth=auth)
if response.status_code != 200:
    print(f"Failed to query Censys API: {response.text}")
    exit(1)

# Parse response from Censys API
json_data = response.json()

# Get the 'result' dictionary from the JSON data
result = json_data['result']

# Get the 'hits' list from the 'result' dictionary
hits = result['hits']

# Create a new list to store the 'ip' values
ip_list = []

# Iterate over the 'hits' list
for item in hits:
    # Check if the 'ip' key exists in the current item
    if 'ip' in item:
        # If it exists, get the list of open ports for the current IP address
        open_ports = [service['port'] for service in item['services']]

        # Add the IP address, its open ports, its certificates, and its name to the list
        ip_list.append({'ip': item['ip'], 'name': item['name'], 'open_ports': open_ports})

# Create a new dictionary with the 'ip' list as a value
data = {'ip_addresses': ip_list}

# Write the dictionary to a JSON file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

