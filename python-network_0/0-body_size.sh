#!/bin/bash
# Displays the size of the body of the response (in bytes) of a URL
curl -s "$1" | wc -c
