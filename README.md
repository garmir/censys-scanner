# Censys Informational Scanner
<p> Python Enumeration tool that uses [Censys's API](https://search.censys.io/api/) to provide relational IPs, open ports, and subdomains when given a domain. A Censys account is required in order to provide a API credentials</p>

### Usage
<p> Tooling can either be used locally provided Python3 libraries are available, or by using the included [dockerfile](dockerfile)</p>

#### Local Usage
<p> Censys credentials can be obtained at (https://censys.io/account/api)

`python3 intelligence_report.py --uid <API_ID> --secret <API_SECRET> --domain <example.net>`

<p> This will output as data.json</p>

#### Docker Usage
<p> Build/run using:</p>

`docker build -t censys-api-script .`

`docker run -it censys-api-script`

<p>You can then proceed as with local usage using the spawned shell, make sure to export the data.json before exiting your container</p>
