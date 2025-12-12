txt = ''
#txt += f'<div class="nav-item" id="{params["id"]}>\n'
txt += f'<div class="nav" id="{params["id"]}">\n'

txt += jayweb.includef(f'{params["ROOT"]}/include/nav-button.py', params["nav-button"], 4)

for child in params["children"]:
    txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["children"][child], 4)

txt += f'</div>\n'
