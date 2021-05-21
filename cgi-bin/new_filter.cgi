#!/usr/bin/env python3
import json
import cgi
from spel import get_new_filter

print("Content-Type: application/json")
print()
print(json.dumps({'filter': get_new_filter()}))
