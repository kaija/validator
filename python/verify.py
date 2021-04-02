#!/usr/bin/env python3
import OpenSSL
from OpenSSL import crypto
import base64
import hashlib

key_file = open("../public.pem", "r")
key = key_file.read()
key_file.close()
pkey = crypto.load_publickey(crypto.FILETYPE_PEM, key)
with open("../sample.bin","rb") as f:
    with open("sign.sha256", "rb") as s:
        x509 = crypto.X509()
        x509.set_pubkey(pkey)
        data = f.read()
        sign = s.read()
        try:
            OpenSSL.crypto.verify(x509, sign, data, "sha256")
            print("Verified OK")
        except:
            print("Verification Failure")

