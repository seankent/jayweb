if "href" not in params:
    params["href"] = "#" 


txt = ''

txt += f'<a href="{params["href"]}" class="nav-button-dropdown">\n'

if "text" in params:
    txt += f'    <div class="nav-button-dropdown-label">\n'
    txt += f'        {params["text"]}\n'
    txt += f'    </div>\n'

if "icon" in params:
    txt += f'    <div class="nav-button-dropdown-chevron">\n'
    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35em", "height": "1.35em"}, 8)
    txt += f'    </div>\n'

#txt += jayweb.includef("./include/button.py", {"width": "1rem", "height": "1rem"}, 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/button.py', {"items": [{"type": "text", "text": params["text"]}]}, 4)

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

