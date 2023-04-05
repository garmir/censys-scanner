# Censys Informational Scanner
Python Enumeration tool that uses [Censys's API](https://search.censys.io/api/) to provide relational IPs, open ports, and subdomains when given a domain. A Censys account is required in order to provide API credentials

### Usage
Tooling can either be used locally provided Python3 libraries are available, or by using the included [dockerfile](https://github.com/garmir/censys-scanner/blob/main/dockerfile)

#### Local Usage
Censys credentials can be obtained at (https://censys.io/account/api)

`python3 intelligence_report.py --uid <API_ID> --secret <API_SECRET> --domain <example.net>`

This will output as data.json

#### Docker Usage
Build/run using:

`docker build -t censys-api-script .`

`docker run -it censys-api-script`

You can then proceed as with local usage using the spawned shell, make sure to export the data.json before exiting your container

### TODO:
* Add more error handling to the code to handle cases where the Censys API returns an error, or if the JSON data is invalid.

* Add more command-line arguments to allow the user to customize the behavior of the program, such as specifying the number of results to return from the API, or the name of the output file.

* Add more functionality to the program, such as making additional API calls to get more information about the IP addresses and subdomains, or performing additional processing on the data before writing it to the JSON file.

* Add some logging to the program to help with debugging and to record important events, such as API calls and data processing.
