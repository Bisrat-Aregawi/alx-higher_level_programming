#!/bin/bash
# Send POST request with field=value pairs
curl -s -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
