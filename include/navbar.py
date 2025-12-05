
txt = ''
txt += f'<div class="navbar">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/navbar-hamburger-menu.py', {"width": "2.5rem", "height": "2.5rem"}, 4)

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params, 4)
txt += f'</div>\n'

