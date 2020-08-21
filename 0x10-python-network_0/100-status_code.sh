#!/bin/bash
# status code 
curl -w "%{response_code}\n" "$1"
