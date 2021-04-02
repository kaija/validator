#!/bin/bash
openssl dgst -sha256 -verify ../public.pem -signature sign.sha256 ../sample.bin
