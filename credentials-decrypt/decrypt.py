#!/usr/bin/env python
# -*- coding:utf-8

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import requests
import json
import base64
import sys

# Create a session
s = requests.Session()

# Load the config file and validate.
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

# Load the private key.
try:
  privateKeyFile = open("czdap.private.key", "r")
  key = RSA.importKey(privateKeyFile.read())
  cipher = PKCS1_v1_5.new(key)
  privateKeyFile.close()
except:
  sys.stderr.write("Error loading private key from file 'czdap.private.key'. Please copy your key into this directory.\n")
  exit(1)

# Get the credentials JSON from CZDAP API.
r = s.get(config['base_url'] + '/user-credentials.json?token=' + config['token'])
if r.status_code != 200:
  sys.stderr.write("Unexpected response from CZDAP. Are you sure your token and base_url are correct in config.json?\n")
  exit(1)
try:
  credsData = json.loads(r.text)
except:
  sys.stderr.write("Unable to parse JSON returned from CZDAP.\n")
  exit(1)

# Decrypt and output.
print "server,username,password"
for creds in credsData:
  piecesJSON = cipher.decrypt(base64.b64decode(creds['credentials']), 0)
  if not piecesJSON:
    print "\nError: Decryption failed, do you have the correct keyfile?"
    exit(1)
  pieces = json.loads(piecesJSON)
  username = unicode(base64.b64decode(pieces[0]), "utf-8")
  password = unicode(base64.b64decode(pieces[1]), "utf-8")
  print ",".join([creds['host'],username,password])
