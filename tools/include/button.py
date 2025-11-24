if "items" not in params:
    params["items"] = []

txt = ''

txt += f'<div class="button">\n'

for i in range(len(params["items"])):

    if params["items"][i]["type"] == "text":
        txt += f'    {params["items"][i]["text"]}\n'

    if params["items"][i]["type"] == "icon":
        txt += jayweb.includef(f'{params["ROOT"]}/tools/include/chevron-down.py', {"width": "1rem", "height": "1rem"}, 4)

txt += f'</div>\n'


#config = {
#    "type": "a",
#    "attr": {"class": "btn", "href": params["href"]},
#    "order": {"text": "0", "icon": "1"},
#    "children": {},
#}
#
#if "text" in params:
#    config["children"]["text"] = {
#        "type": "text",
#        "text": params["text"],
#    }
#
#if "icon" in params:
#    config["children"]["icon"] = {
#        "type": "mount",
#        "filename": "./include/chevron-down.py",
#        "params": {"width": "16px", "height": "16px"}, 
#    }

