import json
from tabulate import tabulate

def convtxt(data):
    txt = ""
    for todo in data:
        txt += "\n"
        for x, y in todo.items():
            txt += f"{x}: {y}\n"
    return txt

def convtable(data):
    if data:
        headers = data[0].keys()
        rows = [list(item.values()) for item in data]
        return tabulate(rows, headers)
    return ""

def convjson(data):
    return json.dumps(data, indent=4)
