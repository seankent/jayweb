
if "nav" not in params:
    params["nav"] = [] 


txt = ''
txt += f'<div class="header">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-logo.py', params["nav-logo"], 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/navbar.py', params["navbar"], 4)
#txt += f'    <div class="nav-hamburger-button">\n'
#txt += f'    </div>\n'
txt += f'    <div class="">\n'
txt += f'    </div>\n'

txt += f'</div>\n'
