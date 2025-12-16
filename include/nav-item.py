txt = ''
#txt += f'<div class="nav-item" id="{params["id"]}>\n'
txt += f'<div class="nav-item" id="{params["id"]}" data-page-id="{params["data-page-id"]}">\n'

txt += jayweb.includef(f'{params["ROOT"]}/include/nav-button.py', params["nav-button"], 4)

for item in params["items"]:
    txt += jayweb.includef(f'{params["ROOT"]}/include/nav-item.py', params["items"][item], 4)

txt += f'</div>\n'
