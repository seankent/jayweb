
txt = ''
txt += f'<div class="navbar">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4)
txt += f'</div>\n'

