
txt = ''
txt += f'<div class="navbar">\n'

for item in params["items"]:
    txt += jayweb.includef(f'{params["ROOT"]}/include/navbar-button.py', params["items"][item], 4)

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-logo.py', params["nav-logo"], 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-toggle.py', {}, 4) 
txt += f'</div>\n'
