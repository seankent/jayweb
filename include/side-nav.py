txt = ''
txt += f'<div class="side-nav">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-item.py', params["nav-item"], 4)
txt += f'</div>\n'
