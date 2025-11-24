if "items" not in params:
    params["items"] = [] 


txt = ''

txt += f'<div class="dropdown">\n'

txt += jayweb.includef(f'{params["ROOT"]}/tools/include/button.py', {"items": [{"type": "text", "text": params["text"]}, {"type": "icon", "icon-type": "chevron-down"}]}, 4)

txt += f'    <div class="dropdown-menu">\n'

for i in range(len(params["items"])):

    txt += f'        <div class="dropdown-menu-item">\n'
    txt += f'           <a href="{params["items"][i]["href"]}">{params["items"][i]["text"]}</a>\n'
    txt += f'        </div>\n'

txt += f'    </div>\n'

txt += f'</div>\n'

#txt += f'    <ul class="dropdown-menu">\n'
#
#for i in range(len(params["items"])):
#
#    txt += f'        <li class="dropdown-menu-item">\n'
#    txt += f'           <a href="{params["items"][i]["href"]}">{params["items"][i]["text"]}</a>\n'
#    txt += f'        </li>\n'
#
#txt += f'    </ul>\n'

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

