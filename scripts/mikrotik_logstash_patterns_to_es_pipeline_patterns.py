#!/bin/env python3


import json

in_file="general_patterns.txt"
out_file="general_patterns.json"

out_obj = {}

for line in open(in_file):
    if line.startswith("#") or line.startswith(" ") or len(line) < 5:
        continue
    name, pattern = line.split(maxsplit=1)
    out_obj[name] = pattern

json.dump(out_obj, open(out_file, "w", encoding="utf-8"))

out_obj.close()
