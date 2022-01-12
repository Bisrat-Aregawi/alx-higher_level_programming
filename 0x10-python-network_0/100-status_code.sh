#!/bin/bash
# Output only the status code of a GET request
curl -s -o /dev/null -w "%{http_code}" "$1"
