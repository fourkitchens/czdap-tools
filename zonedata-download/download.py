#!/usr/bin/env python
# -*- coding:utf-8

import requests
import json
import sys
from urlparse import urlparse
import os

# Create a session
s = requests.Session()

# Load the config file
try:
  configFile = open("config.json", "r")
  config = json.load(configFile)
  configFile.close()
except:
  sys.stderr.write("Error loading config.json file.\n")
  exit(1)
if not config.has_key('token'):
  sys.stderr.write("'token' parameter not found in the config.json file\n")
  exit(1)
if not config.has_key('base_url'):
  sys.stderr.write("'base_url' parameter not found in the config.json file\n")
  exit(1)

# For development purposes, we sometimes run this against an environment with
# basic auth and a self-signed certificate. If these params are present, use
# them. If you're not a developer working on CZDAP itself, ignore these.
if config.has_key('auth_user') and config.has_key('auth_pass'):
  s.auth = (config['auth_user'], config['auth_pass'])
if config.has_key('ssl_skip_verify'):
  s.verify = False

# Get all the files that need to be downloaded using CZDAP API.
r = s.get(config['base_url'] + '/user-zone-data-urls.json?token=' + config['token'])
if r.status_code != 200:
  sys.stderr.write("Unexpected response from CZDAP. Are you sure your token and base_url are correct in config.json?\n")
  exit(1)
try:
  urls = json.loads(r.text)
except:
  sys.stderr.write("Unable to parse JSON returned from CZDAP.\n")
  exit(1)

# Grab each file.
for url in urls:
  r = s.get(config['base_url'] + url)
  if r.status_code == 200:
    parsed_url = urlparse(r.url)
    filename = os.path.basename(parsed_url.path)
    directory = './zonefiles'
    if not os.path.exists(directory):
      os.makedirs(directory)
    path = directory + '/' + filename + '.txt.gz'
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
  else:
    sys.stderr.write("Unexpected HTTP response for URL " + url + "\n")
