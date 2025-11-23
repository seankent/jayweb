
if "nav" not in params:
    params["nav"] = [] 


params["nav"].append({
    "href": "./About",
    "text": "About",
    "icon": "chevron-down",
})

params["nav"].append({
    "href": "./Products",
    "text": "Products",
    "icon": "chevron-down",
})

txt = ''

txt += f'<div class="grid grid-page grid-header">\n'

txt += f'    <div class="grid grid-page grid-header-left">\n'

txt += jayweb.includef("./include/nav-logo.py", {"href": "#", "src": "./../docs/bluejay_devices.svg"}, 8)

txt += f'    </div>\n'

txt += f'    <div class="grid grid-page grid-header-center">\n'

for i in range(len(params["nav"])):
    #txt += jayweb.includef("./include/nav-button.py", params["nav"][i], 8)
    txt += jayweb.includef("./include/nav-button.py", params["nav"][i], 8)

txt += jayweb.includef("./include/nav-dropdown.py", {"text": "Contact", "items": [{"href": "./About", "text": "About"}, {"href": "#", "text": "More"}]}, 8)

txt += f'    </div>\n'

txt += f'    <div class="grid grid-page grid-header-right">\n'
txt += f'    </div>\n'

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

