if "items" not in params:
    params["items"] = []
if "indent" not in params:
    params["indent"] = "1"

txt = ''

txt += f'<div class="side-nav-item" id="{params["id"]}">\n'
#txt += f'    {params["text"]}\n'

#if "icon" in params:
#txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', {"text": params["text"]}, 4)
txt += f'    <div class="side-nav-button">\n'

#if params["items"] != []:
#    txt += f'    <div class="side-nav-button-chevron">\n'
#    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35em", "height": "1.35em"}, 8)
#    txt += f'    </div>\n'

txt += f'        <a href="{params["href"]}" class="side-nav-button-label" style="padding-left: {params["indent"]}em">\n'
#txt += f'            {"&nbsp;"*int(params["indent"]) + params["text"]}\n'
txt += f'            {params["text"]}\n'
txt += f'        </a>\n'

if params["items"] != []:
    txt += f'        <div class="side-nav-button-chevron">\n'
    txt += jayweb.includef(f'{params["ROOT"]}/include/chevron-down.py', {"width": "1.35em", "height": "1.35em"}, 8)
    txt += f'        </div>\n'

txt += f'    </div>\n'

for i in range(len(params["items"])):
    params["items"][i]["indent"] = str(int(params["indent"]) + 1)
    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-item.py', params["items"][i], 4)

#if params["text"][0] == "P":
#    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', {"text": "Base 0"}, 4)
#if params["text"][0] == "P" and int(params["text"][-1]) % 2 == 0:
#    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', {"text": "Base 1"}, 4)
    

#for i in range(len(params["items"])):
#    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', {"text": params["text"]}, 4)
    #txt += f'        <div>\n'
    #txt += f'            Hello\n'
    #txt += f'        </div>\n'


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

