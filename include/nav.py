
txt = ''
txt += f'<div class="nav" id="{params["id"]}">\n'

for i in range(len(params["items"])):
    txt += jayweb.includef(f'{params["ROOT"]}/include/nav-item.py', params["items"][i], 4)

txt += f'</div>\n'

