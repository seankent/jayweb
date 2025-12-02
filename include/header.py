
if "nav" not in params:
    params["nav"] = [] 


txt = ''
txt += f'<div class="header">\n'
txt += jayweb.includef(f'{params["ROOT"]}/include/nav-logo.py', params["nav-logo"], 4)
txt += jayweb.includef(f'{params["ROOT"]}/include/nav.py', params["nav"], 4)
txt += f'</div>\n'
