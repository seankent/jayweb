
txt = ''
txt += f'<div class="nav-menu">\n'
txt += f'    <div class="nav-toggle-wrapper">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 8)
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-cross-button.py', {}, 8)
txt += f'    </div>\n'
txt += f'    <div class="nav-wrapper">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 8)
txt += f'    </div>\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-cross-button.py', {}, 4)
#txt += f'    <div class="nav-cross-button">\n'
#txt += f'    </div>\n'
txt += f'    <div class="">\n'
txt += f'    </div>\n'
txt += f'</div>\n'

