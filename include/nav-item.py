
txt = ''
txt += f'<div class="nav-item">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-button.py', params["nav-button"], 4)

for i in range(len(params["items"])):
    txt += jayweb.includef(f'{params["ROOT"]}/include/nav-item.py', params["items"][i], 4)

txt += f'</div>\n'
