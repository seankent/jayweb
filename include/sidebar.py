

txt = ''
txt += f'<div class="sidebar">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/sidebar-header.py', {}, 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 
txt += f'</div>\n'
