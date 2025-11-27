

config = {}

config["root"] = {
    "sub": {},
}

config["root"]["sub"]["index"] = {
    "sub": {},
}

config["root"]["sub"]["about"] = {
    "sub": {},
}

config["root"]["sub"]["products"] = {
    "sub": {},
}

config["root"]["sub"]["products"]["sub"]["jay40"] = {
    "sub": {},
}

print(config)

def build(config, path = ""):
    params = {}

    params["href"] = path 
    params["items"] = [] 

    for sub in config["sub"]:
        params["items"].append(build(config["sub"][sub], path + "/" + sub))

    return params 
        
params = build(config["root"])

print(params)




