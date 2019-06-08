## Table of contents
* [Minimum  Requirements](#requirements)
* [Setup](#setup)
* [Run](#run)
* [Test](#test)
* [Security Considerations](#security)

## Minimum  Requirements
Ensure below software is installed on the your machine:
* Docker Version 17.05 or higher
* Sign Up with macaddress.io and copy API key from Account -> General page.

## Setup
Checkout code from github and build the container:
```
$ git clone
$ cd macinfo
$ docker build -t macinfo .
```

## Run
Run below command with apikey and mac address.
Following mac address formats are allowed:
- 98:01:a7:a2:df:fd
- 98-01-a7-a2-df-fd
- 9801a7a2dffd
```
$ docker run --rm macinfo --macaddress {MAC ADDRESS} --apikey {YOUR_API_KEY}
```

## Test
Run below commands to test changes in the tool:
```
$ docker build --target=test -t macinfo .  
$ docker run --rm macinfo
```

## Security Considerations
* Tool validates input.
* Tool uses HTTPs to get vendor info.
* API Key Security - Pending :
    * This tool uses API Keys to fetch vendor information which should be stored securely.
    * We can store API Key in Hashcorp Vault instance which encrypts and stores key-value pairs on disk.
    * The tool can be programmed to fetch key-value from vault whenever it runs in exchange of a app tokens provided by vault.
