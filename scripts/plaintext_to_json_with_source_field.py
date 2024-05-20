#!/bin/env python3

import json

out=open("json_check.json", "w")
out_obj=[]

with open("json_check.txt") as file:
    for line in file:
        out_obj.append({"_source": {"message": line}})

json.dump(out_obj, out)
out.close()
