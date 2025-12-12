
txt = ''
txt += f'<body data-nav-id="{params["data-nav-id"]}">\n'
#txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 

#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 

#txt += jayweb.includef(f'{params["ROOT"]}/include/header.py', params["header"], 4) 
#txt += jayweb.includef(f'{params["ROOT"]}/include/nav-menu.py', params["nav-menu"], 4) 

txt += jayweb.includef(f'{params["ROOT"]}/include/navbar.py', params["navbar"], 4) 
txt += jayweb.includef(f'{params["ROOT"]}/include/main.py', params["main"], 4) 

txt += f'<script src="{params["ROOT"]}/include/app.js"></script>\n'
txt += f'</body>\n'


