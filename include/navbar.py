
txt = ''
txt += f'<div class="navbar">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 
txt += f'</div>\n'


