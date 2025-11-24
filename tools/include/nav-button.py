if "href" not in params:
    params["href"] = "#" 


txt = ''

txt += f'<a href="{params["href"]}" class="nav-button">\n'

#txt += jayweb.includef("./include/button.py", {"width": "1rem", "height": "1rem"}, 4)
txt += jayweb.includef(f'{params["ROOT"]}/tools/include/button.py', {"items": [{"type": "text", "text": params["text"]}]}, 4)

txt += f'</a>\n'


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

