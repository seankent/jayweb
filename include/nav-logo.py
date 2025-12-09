if "href" not in params:
    params["href"] = "#" 
if "src" not in params:
    params["src"] = "" 
if "alt" not in params:
    params["alt"] = "" 


txt = ''

txt += f'<div href="{params["href"]}" class="nav-logo">\n'

txt += f'<a href="{params["href"]}" class="nav-logo-button">\n'
txt += f'    <img src="{params["src"]}" alt="{params["alt"]}">\n'
txt += f'</a>\n'

txt += f'</div>\n'

#txt += f'    <img src="./../docs/bluejay_devices.svg" alt="{{ site.title }}" class="nav-logo-img">'



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

