#!/bin/bash
# Show accepted methods of a server
curl -s -I -X OPTIONS "$1" | grep Allow: | cut -d ':' -f 2
