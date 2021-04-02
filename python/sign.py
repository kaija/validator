#!/usr/bin/env python3
import OpenSSL
from OpenSSL import crypto
import base64
import hashlib

key_file = open("../private.pem", "r")
key = key_file.read()
key_file.close()
password = None

if key.startswith('-----BEGIN '):
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key, password)
else:
    pkey = crypto.load_pkcs12(key, password).get_privatekey()

with open("../sample.bin","rb") as f:
    data = f.read()
    sign = OpenSSL.crypto.sign(pkey, data, "sha256") 
    data_base64 = base64.b64encode(sign)
    print (data_base64.decode("utf-8"))
    with open("sign.sha256", "wb") as o:
        o.write(sign)
        o.close()

