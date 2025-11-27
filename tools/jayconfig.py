import re

config = {}

config["root"] = {
    "info": {},
    "sub": {},
    "order": {}, 
}

config["root"]["sub"]["about"] = {
    "info": {},
    "sub": {},
    "order": {}, 
} 

config["root"]["sub"]["products"] = {
    "info": {},
    "sub": {},
    "order": {}, 
} 

print(config)

def build(config, path = ""):
    params = {}

    if path == "":
        params["href"] = "index.html"
    else:
        params["href"] = path + "/index.html"

    params["items"] = [] 

    for subpage in config["sub"]:
        params["items"].append(build(config["sub"][subpage], path + "sub/" + subpage))

    return params

params = build(config["root"])

print(params)

#config["root"]["products"]["jay40"] = {}
#
#config["root"]["products"]["jaybtn"] = {}

#print(config)
#
#def build(config, path = ""):
#    params = {}
#
#    params["href"] = path + "index.html"
#
#    params["items"] = [] 
#
#    for sub in config["sub"]:
#        params["items"].append(build(config["sub"][sub], path + "sub/" + sub + "/"))
#
#    return params 
#
#        
#params = build(config["root"])
#
#print(params)




