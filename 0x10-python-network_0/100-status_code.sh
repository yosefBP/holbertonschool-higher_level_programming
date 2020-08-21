#!/bin/bash
# http_code or response_code
curl -sw "%{response_code}" "$1" -o resp
