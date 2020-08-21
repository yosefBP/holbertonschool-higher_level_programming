#!/bin/bash
# status code or response_code
curl -w "%{http_code}\n" "$1"
