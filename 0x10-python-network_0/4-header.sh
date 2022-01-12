#!/bin/bash
# Get request and show only the body of the response
curl -s -X GET -H 'X-school-User-id: 98' "$1"
