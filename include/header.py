
txt = ''
txt += f'<div class="header">\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/navbar.py', params["navbar"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-logo.py', params["nav-logo"], 4)
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-toggle.py', {}, 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-hamburger-button.py', {}, 4) 
txt += f'</div>\n'
