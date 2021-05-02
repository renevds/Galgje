#!/usr/bin/env python3
import json
import cgi
from galgje import get_new_fitler

print("Content-Type: application/json")
print()
print(json.dumps({'filter': get_new_fitler()}))
