#!/usr/bin/env python

import os
import sys
import argparse
from libs.common import get_mac_info


def format_mac_info(macinfo):
    output = """
    Company: {}
    Country: {}
    """.format(
        macinfo['vendorDetails']['companyName'],
        macinfo['vendorDetails']['countryCode']
    )
    return output


def main():
    usage = """
    macinfo - Retrieves vendor information for a given mac address
    Required Params:
        - API Key
        - Mac Address
    Example:
    """
    parser = argparse.ArgumentParser(description=usage)
    required = parser.add_argument_group('required arguments')

    required.add_argument(
        "-k",
        "--apikey",
        dest="apikey",
        required=True,
        help="""API Key from macaddress.io"""
    )

    required.add_argument(
        "-m",
        "--macaddress",
        dest="macaddress",
        required=True,
        help="""MAC Address"""
    )

    args = parser.parse_args()


    macinfo = get_mac_info(args.apikey, args.macaddress)
    print(format_mac_info(macinfo))


if __name__ == '__main__':
    main()
