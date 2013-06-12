#!/usr/bin/env python
# -*- coding:utf-8

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import json
import base64

privateKeyFile = open("czdap.private.key", "r")
key = RSA.importKey(privateKeyFile.read())
cipher = PKCS1_v1_5.new(key)
privateKeyFile.close()

credsFile = open("credentials.json", "r")
credsData = json.load(credsFile)
credsFile.close()

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
