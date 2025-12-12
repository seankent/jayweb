
txt = ''
txt += f'<div class="nav-toggle">\n'
txt += f'    <div class="nav-toggle-button">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 8)
txt += f'    </div>\n'

txt += f'    <div class="nav-toggle-menu">\n'
txt += f'        <div class="nav-toggle-button">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-cross-button.py', {}, 12)
txt += f'        </div>\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 8)
txt += f'    </div>\n'

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-cross-button.py', {}, 4)
#txt += f'    <div class="nav-cross-button">\n'
#txt += f'    </div>\n'
txt += f'</div>\n'

