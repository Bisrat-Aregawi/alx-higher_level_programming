#!/bin/bash
# Show accepted methods of a server
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
