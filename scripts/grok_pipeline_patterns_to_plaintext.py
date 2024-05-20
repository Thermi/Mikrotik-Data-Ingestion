#!/bin/env python3


# grok processor pattern definitions to flat file script

import json

in_file=open("processor_def.json")
out_file=open("grok_patterns.txt", "w")

js_obj=json.load(in_file)

for processor in js_obj["processors"]:
    if "grok" in processor:
        for key, value in processor["grok"]["pattern_definitions"].items():
            out_file.write(f"{key} {value}\n")

in_file.close()
out_file.close()
