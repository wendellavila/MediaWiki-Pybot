# standard library imports
import json
import os
from typing import List

def read_pagelist(pagelist_path: str) -> List[str]:
    pagelist = []
    with open(pagelist_path, "r") as pagelist_file:
        for line in pagelist_file.readlines():
            pagelist.append(line)
    return pagelist

def write_pagelist(pagelist: List[str], pagelist_path: str, pagelist_mode: str):
    os.makedirs(os.path.dirname(pagelist_path), exist_ok=True)
    with open(pagelist_path, pagelist_mode) as pagelist_file:
        for pagename in pagelist:
            pagelist_file.write("{}\n".format(pagename))

def save_credentials(credentials_path: str, username: str, password: str, url: str):
    if os.path.exists(credentials_path):
        with open(credentials_path) as input_file:
            credentials = json.load(input_file)
    else:
        credentials = {'username':None,'password':None,'url':None}

    credentials['username'] = username if username is not None else credentials['username']
    credentials['password'] = password if password is not None else credentials['password']
    credentials['url'] = url if url is not None else credentials['url']

    os.makedirs(os.path.dirname(credentials_path), exist_ok=True)
    with open(credentials_path, "w") as output_file:
        json.dump(credentials, output_file)