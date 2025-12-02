if "items" not in params:
    params["items"] = []
if "indent" not in params:
    params["indent"] = "1"

txt = ''


txt += f'<div class="side-nav-item" id="{params["id"]}">\n'

txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', params["nav-button"], 8)

#txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-toggle-button.py', params["nav-button"], 8)

#if params["items"] == []:
#    txt += f'    <div class="side-nav-button">\n'
#    txt += f'        <a href="{params["nav-button"]["href"]}" class="side-nav-button-label" style="padding-left: {params["indent"]}em">\n'
#    txt += f'            {params["nav-button"]["text"]}\n'
#    txt += f'        </a>\n'
#    txt += f'    </div>\n'
#else:
#    txt += f'    <div class="side-nav-button side-nav-button-with-icon">\n'
#    txt += f'        <a href="{params["nav-button"]["href"]}" class="side-nav-button-label" style="padding-left: {params["indent"]}em">\n'
#    #txt += f'            {"&nbsp;"*int(params["indent"]) + params["text"]}\n'
#    txt += f'            {params["nav-button"]["text"]}\n'
#    txt += f'        </a>\n'
#    txt += f'        <div class="side-nav-button-chevron">\n'
#    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35em", "height": "1.35em"}, 8)
#    txt += f'        </div>\n'
#    txt += f'    </div>\n'
#
#

for i in range(len(params["items"])):
    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-item.py', params["items"][i], 4)


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

