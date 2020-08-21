#!/bin/bash
# status code or response_code
curl -s -w "%{response_code}\n" "$1"
