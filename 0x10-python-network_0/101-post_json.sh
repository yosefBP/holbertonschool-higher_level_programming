#!/bin/bash
# cURL a JSON file
curl -s -d @"$2" -X POST "$1"
