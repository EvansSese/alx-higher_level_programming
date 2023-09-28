#!/bin/bash
# Curls a resource and returns its body size in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
