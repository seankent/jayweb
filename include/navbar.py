
txt = ''
txt += f'<div class="navbar">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-logo.py', params["nav-logo"], 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-toggle.py', {}, 4) 
txt += f'</div>\n'
