#!/bin/bash
# Script retrives size of content sent by server.
curl -Is "$1" | grep 'Content-Length' | tr -d ' ' | cut -d ':' -f 2
