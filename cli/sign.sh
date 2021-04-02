#!/bin/bash
openssl dgst -sha256 -sign ../private.pem -out sign.sha256 ../sample.bin
base64 sign.sha256
