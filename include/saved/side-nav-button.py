

txt = ''
txt += f'<div class="side-nav-button">\n'

if params["toggle"] == "yes":
    txt += f'    <a class="side-nav-button-text" href="{params["href"]}" style="padding-left: {params["indent"]}rem">\n'
    txt += f'        {params["text"]}\n'
    txt += f'    </a>\n'
    txt += f'    <div class="side-nav-button-chevron">\n'
    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35rem", "height": "1.35rem"}, 4)
    txt += f'    </div>\n'
else:
    txt += f'    <a class="side-nav-button-text" href="{params["href"]}" style="padding-left: {params["indent"]}rem">\n'
    txt += f'        {params["text"]}\n'
    txt += f'    </a>\n'

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

