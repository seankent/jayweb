if "" not in params:
    params["class"] = ""

if "src" not in params:
    params["src"] = ""

if "alt" not in params:
    params["alt"] = ""

config = {
    "type": "img",
    "attr": {"class": params["class"], "src": params["src"], "alt": params["alt"]},
    "order": {},
    "children": {},
}

