#!/usr/bin/env python3
import json
import cgi
from spel import guess_letter

# Lees data verstuurd door JavaScript
parameters = cgi.FieldStorage()
data = json.loads(parameters.getvalue('data'))

print("Content-Type: application/json")
print()
print(json.dumps(guess_letter(data['letter'], data['filter'], data['exclude'])))
