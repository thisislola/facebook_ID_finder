# *********************************** #
#       FB Finder - thisislola      * #
#           February 2019           * #
# *********************************** #

# Run with: python fbid_finder.py https://www.facebook.com/username
# Works with Python 3.x

import requests
import re
import argparse

# Argument Parser 
parser = argparse.ArgumentParser()
parser.add_argument("url", help="It needs a facebook profile URL such as https://www.facebook.com/username")

args = parser.parse_args()
url = args.url

# FB Identification
byte_obj = b'"entity_id":"([0-9]+)"'
id_req= re.compile(byte_obj)
page = requests.get(url)
fb_list = id_req.findall(page.content)

# Weird decoding of a list of bytes? 
fbid = fb_list[0].decode()

# Result
print("[*] The Facebook ID for this account is: ", fbid)
