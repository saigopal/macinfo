import sys
import re
import requests

MAC_URL = 'https://api.macaddress.io/v1?output=json&search={}'


def is_valid_mac(macaddress):
    """Returns True if MAC address is acceptable format.
       Param: macaddress

       Example:
        - ff:ff:ff:ff:ff:ff
        - ff-ff-ff-ff-ff-ff
        - ffffffffffff
    """
    pattern = r'([a-f0-9]{2}[:|\-]{0,1}){5}[a-f0-9]{2}'
    if re.match(pattern, macaddress, re.IGNORECASE):
        return True
    else:
        return False


def get_mac_info(apikey, macaddress):
    """Retrieves vendor info from macaddress.io
       Param: macaddress
       Param: API Key
    """

    if is_valid_mac(macaddress):
        try:
            r = requests.get(
                    url=MAC_URL.format(macaddress),
                    headers={'X-Authentication-Token': apikey},
                    timeout=10
            )
            r.raise_for_status()
            return r.json()
        except (
            requests.exceptions.RequestException,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout
            ) as e:
            print(e)
            sys.exit(1)
    else:
        return 'ERROR: Invalid MAC Format.'
