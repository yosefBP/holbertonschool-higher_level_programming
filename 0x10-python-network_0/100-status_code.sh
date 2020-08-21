#!/bin/bash
# status code 
curl -sw "%{response_code}\n" "$1"
