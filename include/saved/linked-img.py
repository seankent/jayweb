if "href" not in params:
    params["href"] = ""

config = {
    "type": "a",
    "attr": {"href": params["href"]},
    "order": {"img": "0"},
    "children": {},
}

config["children"]["img"] = {
    "type": "mount",
    "filename": "./include/img.py",
    "params": params, 
}

