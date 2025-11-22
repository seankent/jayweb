
config = {
    "type": "button",
    "attr": {"class": "button"},
    "order": {"text": "0"},
    "children": {"text": {}},
}

config["children"]["text"] = {
    "type": "text",
    "text": params["text"],
}

