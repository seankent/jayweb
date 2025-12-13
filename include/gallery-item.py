

txt = ''

txt += f'<a href="{params["ROOT"]}/gen/products/jay40/index.html" class="gallery-item">\n'

#txt += f'    <div class="gallery-box">\n'
#txt += f'    </div>\n'
#txt += f'    <div class="gallery-box">\n'
#txt += f'    </div>\n'

txt += f'     <img class="gallery-item-img" src="{params["ROOT"]}/docs/diag/jay40.svg" alt="">\n'
txt += f'    <div class="gallery-item-text">\n'
txt += f'        Jay40 Developement Board\n'
txt += f'    </div>\n'

txt += f'</a>\n'
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

