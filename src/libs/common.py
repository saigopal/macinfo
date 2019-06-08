import re
import requests

MAC_URL = 'https://api.macaddress.io/v1?output=json&search={}'

def is_valid_mac(macaddress):
    pattern = r'([a-f0-9]{2}[:|\-]{0,1}){5}[a-f0-9]{2}'
    if re.match(pattern, macaddress, re.IGNORECASE):
        return True
    else:
        return False

def get_mac_info(apikey, macaddress):
    if is_valid_mac(macaddress):
        try:
            r = requests.get(
                    url=MAC_URL.format(macaddress),
                    headers={'X-Authentication-Token': apikey},
                    timeout=10
            )
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print(e)
        except requests.exceptions.HTTPError as e:
            print("HTTP ERROR: ", e)
        except requests.exceptions.ConnectionError as e:
            print("Connection ERROR: ", e)
        except requests.exceptions.Timeout as e:
            print("Timeout ERROR: ", e)
    else:
        return 'ERROR: Invalid MAC Format.'
