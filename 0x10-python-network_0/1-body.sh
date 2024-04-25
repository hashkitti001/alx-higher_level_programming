#!/usr/bin/bash
# A script that sends a request to a URL passed as an argument, and displays the body of the response
 curl -sI $1 | grep "Content-Length" | cut -d ' ' -f2