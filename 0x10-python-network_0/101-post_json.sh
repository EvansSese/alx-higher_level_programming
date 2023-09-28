#!/bin/bash
# Posts a JSON
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
