
txt = ''
txt += f'<div class="side-nav-menu">\n'
txt += f'    <div class="side-nav-wrapper">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 8)
txt += f'    </div>\n'
txt += f'</div>\n'

