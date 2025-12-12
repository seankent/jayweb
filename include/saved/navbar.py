
txt = ''
txt += f'<div class="navbar">\n'
#txt += f'    <div class="navbar-button">\n'
#txt += f'    </div>\n'

txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-cross-button.py', {}, 4)

#txt += f'    <div class="navbar-select">\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 4)
#txt += f'    </div>\n'

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 4)
txt += f'</div>\n'

