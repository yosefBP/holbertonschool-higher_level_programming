#!/bin/bash
# cURL POST parameters
curl -s -d '{"email":"hr@holbertonschool.com", "subject":"I will always be here for PLD"}' -H "Content-Type: application/json" -X POST "$1"
