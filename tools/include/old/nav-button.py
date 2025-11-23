if "href" not in params:
    params["href"] = "#" 


config = {
    "type": "a",
    "attr": {"class": "btn", "href": params["href"]},
    "order": {"text": "0", "icon": "1"},
    "children": {},
}

if "text" in params:
    config["children"]["text"] = {
        "type": "text",
        "text": params["text"],
    }

if "icon" in params:
    config["children"]["icon"] = {
        "type": "mount",
        "filename": "./include/chevron-down.py",
        "params": {"width": "16px", "height": "16px"}, 
    }

