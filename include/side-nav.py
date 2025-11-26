txt = ''

txt += f'<div class="side-nav">\n'

for i in range(8):
    #txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', {"text": f"Page {i}"}, 4)
    txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-item.py', {"text": f"Page {i}", "items": [{"text": "Sub 0"}, {"text": "Sub 1", "items": [{"text": "Sub Sub 0"}]}]}, 4)
    #txt += jayweb.includef(f'{params["ROOT"]}/include/side-nav-button.py', {"items": [{"type": "text", "text": params["text"]}, {"type": "icon", "icon-type": "chevron-down"}]}, 4)
    #txt += f'    <div class="side-nav-button">\n'
    #txt += f'    </div>\n'
txt += f'</div>\n'
#
#config = {
#    "type": "div",
#    "attr": {"class": "grid grid-page grid-header"},
#    "order": {"header-left": "0", "header-right": "1", "header-center": "0"},
#    "children": {"header-left": {}, "header-right": {}, "header-center": {}},
#}
#
#config["children"]["header-left"] = {
#    "type": "div",
#    "attr": {"class": "grid grid-page grid-header-left"},
#    "order": {"logo": "0"},
#    "children": {},
#}
#
#config["children"]["header-left"]["children"]["logo"] = {
#    "type": "mount",
#    "filename": "./include/img.py",
#    "params": {"class": "", "src": "./include/bluejay_devices.svg"}, 
#}
#
#
#
#config["children"]["header-center"] = {
#    "type": "div",
#    "attr": {"class": "grid grid-page grid-header-center"},
#    "order": {},
#    "children": {},
#}
#
#buttons = ["About", "Products", "Docs"]
#
#for i in range(len(buttons)):
#    button = buttons[i]
#
#    config["children"]["header-center"]["order"][button] = str(i); 
#
#    config["children"]["header-center"]["children"][button] = {
#        "type": "mount",
#        "filename": "./include/nav-button.py",
#        "params": {"href": f"./{button}", "text": button, "icon": "chevron-down"}, 
#    }
#
#config["children"]["header-right"] = {
#    "type": "div",
#    "attr": {"class": "grid grid-page grid-header-right"},
#    "order": {},
#    "children": {},
#}

